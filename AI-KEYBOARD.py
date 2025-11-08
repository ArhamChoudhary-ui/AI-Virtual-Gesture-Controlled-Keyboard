import cv2
from cvzone.HandTrackingModule import HandDetector
from pynput.keyboard import Controller
import time

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)
time.sleep(1)

detector = HandDetector(detectionCon=0.8, maxHands=1)
keyboard = Controller()
finalText = ""

caps = False

keys_layout = [
    ["Q","W","E","R","T","Y","U","I","O","P"],
    ["A","S","D","F","G","H","J","K","L"],
    ["Z","X","C","V","B","N","M"],
]

special_keys = ["CAPS", "SPACE", "BACK", "CLEAR"]

class Button:
    def __init__(self, pos, text, size):
        self.pos = pos
        self.text = text
        self.size = size
        self.pressed = False

buttonList = []

def create_buttons():
    global buttonList
    buttonList = []

    screen_center = 640
    y_start = 260
    size = 85
    gap = 12

    for idx, row in enumerate(keys_layout):
        row_width = len(row) * size + (len(row)-1) * gap
        x_start = screen_center - row_width // 2
        y = y_start + idx * (size + gap)

        for j, key in enumerate(row):
            x = x_start + j * (size + gap)
            buttonList.append(Button([x, y], key, (size, size)))

    y = y_start + 3 * (size + gap) + 20
    special_sizes = {
        "CAPS": size * 2,
        "SPACE": size * 5,
        "BACK": size * 2,
        "CLEAR": size * 2,
    }

    row_width = sum(special_sizes[k] for k in special_keys) + gap * (len(special_keys)-1)
    x_start = screen_center - row_width // 2
    x = x_start

    for key in special_keys:
        w = special_sizes[key]
        buttonList.append(Button([x, y], key, (w, size)))
        x += w + gap

create_buttons()

def drawRoundedRectangle(img, pt1, pt2, color, radius=18):
    x1, y1 = pt1
    x2, y2 = pt2
    overlay = img.copy()

    cv2.rectangle(overlay, (x1 + radius, y1), (x2 - radius, y2), color, -1)
    cv2.rectangle(overlay, (x1, y1 + radius), (x2, y2 - radius), color, -1)

    cv2.circle(overlay, (x1 + radius, y1 + radius), radius, color, -1)
    cv2.circle(overlay, (x2 - radius, y1 + radius), radius, color, -1)
    cv2.circle(overlay, (x1 + radius, y2 - radius), radius, color, -1)
    cv2.circle(overlay, (x2 - radius, y2 - radius), radius, color, -1)

    return cv2.addWeighted(overlay, 0.90, img, 0.10, 0)

def drawAll(img):
    for button in buttonList:
        x, y = button.pos
        w, h = button.size

        base = (55, 55, 55)
        pressed = (150, 40, 200)

        if button.text == "CAPS" and caps:
            color = (200, 80, 50)
        else:
            color = pressed if button.pressed else base

        img = drawRoundedRectangle(img, (x, y), (x + w, y + h), color)

        text = button.text
        tsize = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, 0.8, 2)[0]
        tx = x + (w - tsize[0]) // 2
        ty = y + (h + tsize[1]) // 2

        cv2.putText(img, text, (tx, ty),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8,
                    (255, 255, 255), 2)

    return img

lastPress = 0
pressDelay = 0.30

while True:
    ret, img = cap.read()
    img = cv2.flip(img, 1)
    hands, img = detector.findHands(img, flipType=False)

    if hands:
        lm = hands[0]["lmList"]
        dist, _, _ = detector.findDistance(lm[4][:2], lm[8][:2], img)
        pinch = dist < 40

        for button in buttonList:
            x, y = button.pos
            w, h = button.size

            if x < lm[8][0] < x + w and y < lm[8][1] < y + h:
                if pinch and time.time() - lastPress > pressDelay:
                    lastPress = time.time()
                    button.pressed = True

                    if button.text == "CLEAR":
                        finalText = ""

                    elif button.text == "BACK":
                        finalText = finalText[:-1]

                    elif button.text == "SPACE":
                        finalText += " "
                        keyboard.press(" ")

                    elif button.text == "CAPS":
                        caps = not caps

                    else:
                        char = button.text.upper() if caps else button.text.lower()
                        finalText += char
                        keyboard.press(char)

    img = drawAll(img)

    cv2.rectangle(img, (60, 80), (1220, 160), (40, 40, 40), -1)
    cv2.putText(img, finalText[-40:], (90, 140),
                cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 3)

    cv2.putText(img, "Press Q to Quit", (50, 700),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)

    cv2.imshow("AI Virtual Keyboard - Optimized", img)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

    for b in buttonList:
        b.pressed = False

cap.release()
cv2.destroyAllWindows()
