# 🖐 Hand Gesture-Based System Controller

A real-time hand gesture recognition system that allows users to control **system volume** and **screen scrolling** using only their hand gestures. Built with **MediaPipe**, **scikit-learn**, and **OpenCV**, this lightweight Python project is suitable for productivity, accessibility enhancement, or fun gesture-based interaction demos.

---

## 🚀 Features

- ✋ Hand gesture recognition using Mediapipe (21 landmark points)
- 🔊 Volume Up / Volume Down control via gestures
- ⬆️⬇️ Scroll Up / Scroll Down (useful in browsers, PDFs, etc.)
- 🧠 Trainable KNN model (`scikit-learn`) for user-defined gestures
- 🎯 Modular design with easy-to-extend gesture mapping
- 💻 Optional Jupyter notebook for retraining and experimentation

---

## 📁 Folder Structure
```
Hand-Gesture-Based-System-Controller/
├── src/ # Main real-time recognizer & system control logic
│ ├── gesture_recognizer.py
│ └── system_control.py
├── data/ # Gesture dataset CSV (optional upload)
│ └── gesture_data.csv
├── models/ # Trained KNN + LabelEncoder
│ ├── knn_model.joblib
│ └── label_encoder.joblib
├── notebooks/ # Jupyter notebook for training
│ └── train_gesture_knn.ipynb
├── record_gesture.py # Tool to record gestures to CSV
├── requirements.txt # Project dependencies
└── README.md
```
---

##  🔧 Supported Gestures

Gesture Label	Function
- volume_up	Increase system volume 🔊
- volume_down	Decrease system volume 🔉
- scroll_up	Scroll screen up ⬆️
- scroll_down	Scroll screen down ⬇️

You can extend this list by modifying record_gesture.py, retraining the model, and updating system_control.py.

---

## 💡 Future Ideas

- Add support for play/pause, next track, or screenshot with more gestures
- Port to Android using MediaPipe SDK + Kotlin
- Add WebUI to train gestures from browser
