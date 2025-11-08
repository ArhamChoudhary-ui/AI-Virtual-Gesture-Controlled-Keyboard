# AI Virtual Gesture-Controlled Keyboard

A real-time **hand-gesture-based virtual keyboard** built using **Python, OpenCV, and CVZone**. Users can type by performing a **thumb–index finger pinch gesture** to press keys. The keyboard includes CAPS, Space, Backspace, Clear, rounded UI buttons, and a symmetric layout.

---

## 🚀 Features

* ✅ Hand gesture detection using **CVZone HandDetector**
* ✅ **Pinch to click** (thumb + index)
* ✅ Clean **dark UI** with rounded keys
* ✅ Perfectly **centered & symmetric layout**
* ✅ CAPS toggle
* ✅ Space, Backspace, Clear
* ✅ Smooth performance (optimized)
* ✅ Real-time typing output box

---

## 🛠️ Tech Stack

* **Python 3**
* **OpenCV**
* **CVZone**
* **Pynput**

---

## 📦 Installation

```bash
pip install opencv-python cvzone pynput
```

---

## ▶️ Run the App

```bash
python main.py
```

---

## 📁 Project Structure

```
📂 VirtualKeyboard
 ├── main.py       # Main application code
 ├── README.md     # Project documentation
```

---

## 🎮 Controls

| Action         | Gesture                    |
| -------------- | -------------------------- |
| Press Key      | Thumb + Index Finger Pinch |
| Type Lowercase | CAPS off                   |
| Type Uppercase | CAPS on                    |
| Backspace      | Press BACK                 |
| Clear All      | Press CLEAR                |
| Space          | Press SPACE                |
| Quit App       | Press Q                    |

---

## 🧠 How It Works

* Detects hand landmarks using **CVZone HandDetector**.
* Tracks **Index Tip (8)** and **Thumb Tip (4)**.
* Measures distance.
* If distance < threshold → **key press event**.
* UI is drawn each frame using custom rounded rectangles.

---

## 📸 Demo Image (optional)

You can add a screenshot of your keyboard UI here.

```
![Virtual Keyboard Demo](demo.jpg)
```

---

## ✅ Future Improvements

* Add number row
* Add emoji panel
* Add sound feedback
* Add word prediction (AI-based)
* Save typed text to file

---

## ⭐ Show Support

If you like this project, consider giving it a **star** on GitHub!

---

## 👤 Author

**Arham** – Gesture-based interaction enthusiast.
