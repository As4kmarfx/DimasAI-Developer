import pyautogui
import keyboard

def main():
    print("Program dimulai. Gunakan tombol 'Q' untuk keluar.")
    
    while True:
        if keyboard.is_pressed('q'):
            print("Program berakhir.")
            break
        
        if keyboard.is_pressed('left'):
            pyautogui.move(-10, 0, duration=0.1)  # Geser mouse ke kiri sebanyak 10 piksel
        elif keyboard.is_pressed('right'):
            pyautogui.move(10, 0, duration=0.1)   # Geser mouse ke kanan sebanyak 10 piksel
        # Tambahkan kondisi dan perintah sesuai keinginan Anda
        
        # Pastikan Anda telah mengatur durasi untuk memberikan waktu pada pergerakan mouse.
        
if __name__ == "__main__":
    main()
