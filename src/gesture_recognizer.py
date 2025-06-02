import cv2
import mediapipe as mp
import numpy as np
import joblib
from system_control import volume_up, volume_down, scroll_up, scroll_down

# 載入模型與標籤編碼器
knn = joblib.load("knn_model.joblib")
label_encoder = joblib.load("label_encoder.joblib")

# 初始化 Mediapipe
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)

# 啟動攝影機
cap = cv2.VideoCapture(0)
print("🖐 開始即時手勢辨識，按下 'q' 鍵結束")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # 翻轉畫面與轉換格式
    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb)

    gesture_name = "No Hand"

    if results.multi_hand_landmarks:
        hand_landmarks = results.multi_hand_landmarks[0]
        mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

        # 取得 landmark 特徵
        landmarks = hand_landmarks.landmark
        x = [lm.x for lm in landmarks]
        y = [lm.y for lm in landmarks]
        z = [lm.z for lm in landmarks]
        feature = np.array(x + y + z).reshape(1, -1)

        # 預測手勢類別
        prediction = knn.predict(feature)
        gesture_name = label_encoder.inverse_transform(prediction)[0]

        # 根據手勢執行對應操作
        if gesture_name == "volume_up":
            volume_up()
        elif gesture_name == "volume_down":
            volume_down()
        elif gesture_name == "scroll_up":
            scroll_up()
        elif gesture_name == "scroll_down":
            scroll_down()

    # 顯示辨識結果
    cv2.putText(frame, f"Gesture: {gesture_name}", (10, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 0), 3)
    cv2.imshow("Gesture Recognizer", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 關閉攝影機
cap.release()
cv2.destroyAllWindows()
