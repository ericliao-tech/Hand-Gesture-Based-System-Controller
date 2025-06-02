import cv2
import mediapipe as mp
import csv
import os

# 初始化 mediapipe
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

# Gesture label 對應表
label_map = {
    '1': 'volume_up',   #Thumbs up
    '2': 'volume_down', #Thumbs down
    '3': 'scroll_up',   #Two fingers up
    '4': 'scroll_down'  #Two fingers down
}

# 資料儲存路徑
output_file = "gesture_data.csv"
header_written = os.path.exists(output_file)

# 開啟 CSV 檔案
csv_file = open(output_file, mode='a', newline='')
csv_writer = csv.writer(csv_file)

# 寫入表頭（第一次啟動）
if not header_written:
    header = [f'x{i}' for i in range(21)] + [f'y{i}' for i in range(21)] + [f'z{i}' for i in range(21)] + ['label']
    csv_writer.writerow(header)

# 啟動攝影機
cap = cv2.VideoCapture(0)
with mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7) as hands:
    print("✅ 準備好了！請用手做出指定手勢並按下對應按鍵 1~4, 按 q 結束")
    
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # 翻轉 + 轉為 RGB
        frame = cv2.flip(frame, 1)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(rgb_frame)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

        cv2.imshow('Record Gestures (按 1~4 鍵)', frame)

        key = cv2.waitKey(1) & 0xFF
        key_char = chr(key)

        if key_char in label_map and results.multi_hand_landmarks:
            landmarks = results.multi_hand_landmarks[0].landmark
            x_list = [lm.x for lm in landmarks]
            y_list = [lm.y for lm in landmarks]
            z_list = [lm.z for lm in landmarks]
            row = x_list + y_list + z_list + [label_map[key_char]]
            csv_writer.writerow(row)
            print(f"✅ 已記錄 1 筆資料：{label_map[key_char]}")

        elif key_char == 'q':
            print("👋 程式結束，資料已儲存")
            break

# 結束清理
csv_file.close()
cap.release()
cv2.destroyAllWindows()
