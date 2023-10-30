import cv2
import pyautogui
import mediapipe as mp  
import logging  # Import modul logging

# Set level logging ke INFO
logging.basicConfig(level=logging.INFO)

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.2, min_tracking_confidence=0.2)

# Mendapatkan ukuran layar
screen_width, screen_height = pyautogui.size()

# Inisialisasi video capture
cap = cv2.VideoCapture(0)

# Inisialisasi variabel tindakan gestur
is_flexed = False
is_hold_and_move = False
is_swiping = False

# Koordinat awal posisi jari tengah
start_swipe_y = 0

while True:
    # Baca frame dari webcam
    ret, frame = cap.read()

    # Membalikkan gambar secara horizontal
    frame = cv2.flip(frame, 1)

    # Ubah warna menjadi RGB
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    image.flags.writeable = False

    # Deteksi tangan
    results = hands.process(image)

    # Gambar landmark tangan jika terdeteksi
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Mendapatkan koordinat pusat telapak tangan
            center_x = int(hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].x * screen_width)
            center_y = int(hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].y * screen_height)

            # Mendapatkan posisi jari telunjuk
            index_finger_x = int(hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x * screen_width)
            index_finger_y = int(hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y * screen_height)

            # Gambar landmark tangan
            mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Deteksi tindakan gestur
            if hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_DIP].y < hand_landmarks.landmark[
                mp_hands.HandLandmark.INDEX_FINGER_PIP].y:
                is_flexed = True
                cv2.putText(image, 'Gesture: Pindah', (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                
                # Jika sedang mengepakkan jari, mulai deteksi gestur usap
                if not is_swiping:
                    is_swiping = True
                    start_swipe_y = index_finger_y
            elif hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_DIP].y > hand_landmarks.landmark[
                mp_hands.HandLandmark.INDEX_FINGER_PIP].y and is_flexed:
                is_hold_and_move = True
                cv2.putText(image, 'Gestur: Jeda Tangan', (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                is_swiping = False
            else:
                is_swiping = False

            # Deteksi gestur tangan usap
            if is_swiping:
                # Tentukan ambang batas perpindahan untuk menghindari jitter
                threshold = 20
                
                # Hitung perpindahan jari tengah
                finger_displacement = index_finger_y - start_swipe_y

                # Geser ke atas
                if finger_displacement < -threshold:
                    pyautogui.scroll(1)  # Geser ke atas
                    cv2.putText(image, 'Gesture: Usap ke atas', (20, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                # Geser ke bawah
                elif finger_displacement > threshold:
                    pyautogui.scroll(-1)  # Geser ke bawah
                    cv2.putText(image, 'Gesture: Usap ke bawah', (20, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    # Menggerakkan kursor berdasarkan tindakan gestur
    if is_flexed and not is_hold_and_move:
        pyautogui.click(x=center_x, y=center_y)
        is_flexed = False
    elif is_hold_and_move:
        pyautogui.moveTo(x=center_x, y=center_y)
        is_hold_and_move = False

    # Tampilkan frame
    cv2.imshow('Tangan Trak', cv2.cvtColor(image, cv2.COLOR_RGB2BGR))

    # Periksa tombol 'q' untuk keluar dari loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Setelah keluar dari loop, lepaskan sumber daya
cap.release()
cv2.destroyAllWindows()
