from PIL import ImageTk, Image 
import time, re, random, subprocess, keyboard, tkinter as tk,tkinter as tk

def close_notepad():
    subprocess.call("taskkill /F /IM notepad.exe", shell=True)


def on_entry_change(event):
    if input_entry.get().strip():
        send_button.config(state=tk.NORMAL)
    else:
        send_button.config(state=tk.DISABLED)

    results = data.get("items", [])
    if results:
        return results[0].get("snippet", "")
    else:
        return "Maaf, saya tidak menemukan hasil pencarian untuk pertanyaan Anda."

def buka_aplikasi():
    subprocess.Popen('notepad.exe')  # Ubah 'notepad.exe' dengan path aplikasi catatan yang diinginkan

def tulis_kalimat(kalimat): 
    time.sleep(2)  # Beri waktu untuk aplikasi catatan terbuka
    keyboard.write(kalimat, delay=0.01)

# Contoh penggunaan
kalimat = "Halo, Aku DimasAi! Aku adalah program ChatBot untuk semua orang, dan ini adalah bersumber terbuka yang artinya bebas untuk membantu melengkapi program ini!"
buka_aplikasi()
tulis_kalimat(kalimat)

def clear_text():
    chat_box.delete("1.0", tk.END)

def copy_text():
    selected_text = chat_box.selection_get()
    window.clipboard_clear()
    window.clipboard_append(selected_text)

def cut_text():
    selected_text = chat_box.selection_get()
    window.clipboard_clear()
    window.clipboard_append(selected_text)
    chat_box.delete("sel.first", "sel.last")

def paste_text():
    clipboard_text = window.clipboard_get()
    chat_box.insert(tk.INSERT, clipboard_text)

def show_about_window():
    about_text = "Chatai, aplikasi buatan Raihan, seorang siswa SMA 15 Tangerang, memungkinkan siswa saling berkomunikasi dengan mudah dan efisien. Dilengkapi dengan fitur-fitur kecerdasan buatan, Chatai memberikan respons yang akurat dan mampu memahami konteks percakapan. Selain itu, aplikasi ini juga menyediakan opsi respons seperti heheheh untuk menciptakan suasana santai dan menyenangkan."
    chat_box.insert(tk.END, "DimasAI: Tentang\n")
    animate_typing(about_text + "\n")

def select_all_text(event=None):
    chat_box.tag_add(tk.SEL, "1.0", tk.END)
    return "break"

def animate_typing(text):
    for char in text:
        chat_box.insert(tk.END, char)
        chat_box.see(tk.END)
        chat_box.update()
        time.sleep(0.05)

def animate_text(text_widget, text):
    for char in text:
        text_widget.insert(tk.END, char)
        text_widget.update()
        time.sleep(0.02)

class MyAI:
    def __init__(self):
        # Inisialisasi AI
        pass

    def create_image_from_text(self, text, font_size=18, image_width=500, image_height=200, background_color=(255, 255, 255), text_color=(0, 0, 0), font_path="arial.ttf", output_path="output.png"):
        # Membuat objek Image dengan ukuran dan latar belakang yang ditentukan
        image = Image.new("RGB", (image_width, image_height), background_color)


        # Menyimpan image ke file
        image.save(output_path)

        # Menampilkan pesan sukses
        print("Image berhasil dibuat dan disimpan di:", output_path)

    def process_text(self, input_text):
        # Logika AI untuk memproses teks
        self.create_image_from_text(input_text)
#===================2023=============( Mess)
def saat_ditutup():
    if messagebox.askokcancel("Keluar", "Apakah Anda yakin ingin keluar?"):
        # Tutup aplikasi yang terbuka atau lakukan tugas pembersihan jika diperlukan
        window.destroy()
#===================2023=============
def respond(event=None):
    user_input = input_entry.get()
    chat_box.insert(tk.END, "User: " + user_input + "\n")
    input_entry.delete(0, tk.END)
    
    if user_input.lower() == "tutup":
        window.destroy()
        return

    if "tutup" in user_input.lower() or "keluar" in user_input.lower():
        window.destroy()

    response = generate_response(user_input)
    if response.startswith("buatlah kode"):
        code_type = response.split("buatlah kode")[1].strip()
        show_code(code_type)
    else:
        animate_text(chat_box, "DimasAI: " + response + "\n")
    chat_box.see(tk.END)

def show_code(code_type):
    if code_type == "tabel":
        code = '''import pandas as pd

# Membuat DataFrame
data = {'Nama': ['John', 'Jane', 'Tom'],
        'Usia': [25, 30, 35],
        'Kota': ['Jakarta', 'Surabaya', 'Bandung']}

df = pd.DataFrame(data)

# Menampilkan DataFrame
print(df)
'''
    else:
        code = "# Tulis kode " + code_type + " di sini"
    
    chat_box.insert(tk.END, "DimasAI: Kode " + code_type + "\n")
    animate_typing(code + "\n")

def open_application(app_name):
    try:
        subprocess.Popen(app_name)
        return "Aplikasi {} berhasil dibuka.".format(app_name)
    except FileNotFoundError:
        return "Aplikasi {} tidak ditemukan.".format(app_name)
    
def generate_response(question):
    if "halo" in question.lower() or "hai" in question.lower() or "oi" in question.lower() or "hi" in question.lower() or "oha!" in question.lower() or "HOI!!!!" in question.lower():
        return "Halo! Ada yang bisa saya bantu?"
    elif "apa yang ada di gambar ini" in question.lower() or "deskripsikan gambar ini" in question.lower():
        return "Maaf, saya tidak dapat melihat gambar. Bisakah Anda memberikan deskripsi atau konteks tentang gambar tersebut?"
    elif "siapa nama kamu" in question.lower():
        return "Saya adalah DimasAI, Dikembangkan oleh anak SMA yaitu Raihan dari SMA 15 Kota Tangerang"
    
    elif "apa kabar" in question.lower():
        return "Saya adalah AI, jadi saya tidak memiliki perasaan. Tapi terima kasih telah bertanya!"
    elif "terima kasih" in question.lower():
        return "Sama-sama, senang bisa membantu!"
    elif "apakah kamu manusia" in question.lower():
        return "Tidak, saya adalah program komputer yang dikembangkan oleh INDESU."
    elif "tau ngewe?" in question.lower() or "ngewe" in question.lower() or "bangsat" in question.lower() or "bajingan" in question.lower() or "kontl" in question.lower() or "kontol" in question.lower() or "anj" in question.lower() or "anjing" in question.lower() or "bego" in question.lower():
        return "Maaf, pertanyaan tersebut tidak pantas dan tidak relevan."
    elif "apa hobi kamu" in question.lower():
        return "Sebagai AI, saya tidak memiliki hobi seperti manusia. Saya dirancang untuk membantu menjawab pertanyaan."
    elif "bagaimana cara mengenali objek pada gambar" in question.lower() or "bagaimana cara mendeteksi objek pada gambar" in question.lower():
        return "Ada beberapa pendekatan yang dapat digunakan untuk mengenali objek pada gambar, seperti menggunakan teknik computer vision dengan pendekatan klasifikasi atau pendekatan deteksi objek dengan menggunakan algoritma seperti YOLO atau SSD."
    elif "apa itu image classification" in question.lower() or "apa yang dimaksud dengan klasifikasi gambar" in question.lower():
        return "Image classification atau klasifikasi gambar adalah tugas dalam computer vision untuk mengidentifikasi dan mengkategorikan objek atau elemen pada gambar ke dalam kelas yang telah ditentukan."
    elif "apa itu object detection" in question.lower() or "apa yang dimaksud dengan deteksi objek" in question.lower():
        return "Object detection atau deteksi objek adalah tugas dalam computer vision untuk mengidentifikasi dan memperoleh lokasi serta kelas dari objek yang ada pada gambar."
    elif "apa itu computer vision" in question.lower() or "apa yang dimaksud dengan computer vision" in question.lower():
        return "Computer vision adalah cabang ilmu komputer yang berfokus pada pemrosesan, analisis, dan pemahaman gambar dan video oleh komputer. Tujuannya adalah untuk mengembangkan sistem yang dapat melihat dan memahami dunia seperti yang dilakukan oleh manusia."
    elif "maaf" in question.lower():
        return "Maaf, saya tidak dapat menjawab pertanyaan tersebut. Apakah ada yang lain yang bisa saya bantu?"
    elif "berapa umur kamu" in question.lower():
        return "Sebagai AI, saya tidak memiliki umur. Saya hanya dilahirkan saat program ini dijalankan."
    elif "apa yang bisa kamu lakukan" in question.lower():
        return "Saya dapat membantu menjawab pertanyaan, memberikan informasi, dan melakukan tugas-tugas tertentu."
    elif "Tapir?" in question.lower():
        return "Maaf, kalimat tersebut tidak tepat!"
    elif "Maaf" in question.lower():
        return "Baik tidak maslaah, semua orang pasti mengalami masalah.. silahkan beri pertanyaan yang relevan!"
    elif "siapa nama kamu" in question.lower() or "siapa kamu" in question.lower() or "namamu siapa" in question.lower():
        return "Saya DimasAI, asisten virtual buatan Raihan."
    elif "apa kabar" in question.lower() or "gimana kabar" in question.lower() or "kabar kamu" in question.lower():
        return random.choice(["Kabar saya baik, terima kasih.", "Saya baik-baik saja.", "Saya selalu siap membantu!"])
    elif "terimakasih" in question.lower() or "makasih" in question.lower() or "thanks" in question.lower():
        return random.choice(["Sama-sama!", "Senang bisa membantu.", "Tidak masalah.", "Terima kasih kembali!"])
    elif "ada yang bisa kamu bantu" in question.lower() or "bisa tolong" in question.lower() or "tolong bantu" in question.lower():
        return "Tentu, apa yang bisa saya bantu?"
    elif "buatlah kode" in question.lower() or "tulis kode" in question.lower() or "code" in question.lower():
        return "Silakan tentukan jenis kode yang ingin Anda buat."
    elif "buatlah kode contoh html" in question.lower() or "contoh kode html"in question.lower() or "buat kode html" in question.lower():
        return '''Baiklah, ini dia contoh kode HTML:

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    
</body>
</html>
'''
    elif "ok makasih" in question.lower() or "makasih kodenya" in question.lower():
        return "Sama - Sama, Semoga Bisa Membantu. jangan sungkan untuk bertanya hal lainnya!"
    if "buka aplikasi" in question.lower():
        app_name = re.findall(r"buka aplikasi (.+)", question.lower())[0]
        return open_application(app_name)
    elif "ok!" in question.lower() or "Relevan!" in question.lower():
        return "Terima Kasih sudah memberi penilaian!. jangan sungkan untuk bertanya hal lainnya!"
    elif "berapa" in question.lower() and "?" in question:
        expression = re.findall(r'\bberapa\s*([\d+\-*/\s]+)\?', question.lower())
        if expression:
            return calculate(expression[0])
    return "Terima kasih atas pertanyaannya! Saya belum diprogram untuk merespons pertanyaan itu. Silakan ajukan pertanyaan lain atau berikan pertanyaan yang lebih relevan."
    

def calculate(expression):
    try:
        result = eval(expression)
        return str(result)
    except:
        try:
            result = (expression)
            return str(result)
        except:
            return "Maaf, tidak dapat menghitung hasil dari operasi tersebut."
        
def show_settings_menu():
    settings_menu = tk.Toplevel(window)
    settings_menu.title("Setelan")
    settings_menu.geometry("300x200")
    settings_menu.configure(background="#f0f0f0")

    # Kode pengaturan opsi setelan lainnya ...

    save_button = tk.Button(settings_menu, text="Simpan", command=save_settings, bg="#4CAF50", fg="white", font=("SF Pro", 12), relief=tk.RAISED)
    save_button.pack()
    
def save_settings():
    selected_font = font_var.get()
    selected_language = language_var.get()
    selected_color = color_var.get()
    selected_style = style_var.get()

# Define global variables
font_var = None
language_var = None
color_var = None
style_var = None

# Fungsi untuk menampilkan tentang aplikasi
def show_about_window():
    about_text = "Chatai, aplikasi buatan Raihan, seorang siswa SMA 15 Tangerang, memungkinkan siswa saling berkomunikasi dengan mudah dan efisien. Dilengkapi dengan fitur-fitur kecerdasan buatan, Chatai memberikan respons yang akurat dan mampu memahami konteks percakapan. Selain itu, aplikasi ini juga menyediakan opsi respons seperti heheheh untuk menciptakan suasana santai dan menyenangkan."
    about_window = tk.Toplevel(window)
    about_window.title("Tentang")
    about_window.geometry("300x200")
    about_label = tk.Label(about_window, text=about_text, font=("SF Pro", 12))
    about_label.pack(padx=10, pady=10)

# Fungsi untuk menampilkan jendela "Tentang"
def show_about_window():
    about_window = tk.Toplevel(window)
    about_window.title("Tentang")
    about_window.geometry("300x150")
    about_window.configure(background="#f0f0f0")

    about_label = tk.Label(about_window, text="DimasAi ialah salah satu Katokasi Berkotal Ai , APl ia dapat berkomunikasi ke smua org!.", bg="#f0f0f0", padx=10, pady=10)
    about_label.pack()

# Fungsi untuk menampilkan jendela "Versi"
def show_version_window():
    version_window = tk.Toplevel(window)
    version_window.title("Versi")
    version_window.geometry("300x150")
    version_window.configure(background="#f0f0f0")

    version_label = tk.Label(version_window, text="Versi: 1.0", bg="#f0f0f0", padx=10, pady=10)
    version_label.pack()

# Membuat jendela aplikasi
window = tk.Tk()
window.title("DimasAI | 1.0")
window.geometry("400x500")
window.resizable(False, False)
window.configure(bg="white")

#Mess2
# Ikutkan fungsi saat_ditutup ke peristiwa tutup jendela
window.protocol("WM_DELETE_WINDOW", saat_ditutup)
#Mess2

# Mengubah warna latar belakang dan warna teks pada kotak chat
chat_box = tk.Text(window, bg="#000000", fg="white", font=("SF Pro", 12), wrap=tk.WORD)
chat_box.pack(fill=tk.BOTH, expand=True)

# Mengubah warna teks pada kolom input
input_entry = tk.Entry(window, bg="#FFFFFF", fg="#000000", font=("SF Pro", 12))
input_entry.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Mengaktifkan tombol "Enter" dan "Shift + Enter"
input_entry.bind("<Return>", respond)
input_entry.bind("<Shift-Return>", respond)

# Membuat tombol kirim dengan desain yang menarik
send_button = tk.Button(window, text="Kirim", command=respond, bg="#4CAF50", fg="white", font=("SF Pro", 12), relief=tk.RAISED)
send_button.pack(side=tk.RIGHT, padx=10, pady=10)

# Menambahkan tombol "Bersihkan"
clear_button = tk.Button(window, text="Bersihkan", command=clear_text, bg="#FF0000", fg="white", font=("SF Prol", 12), relief=tk.RAISED)
clear_button.pack(side=tk.RIGHT, padx=10, pady=10)

# Menambahkan tombol "Tentang"
about_button = tk.Button(window, text="Tentang", command=show_about_window, bg="#1E90FF", fg="white", font=("SF Pro", 12), relief=tk.RAISED)
about_button.pack(side=tk.LEFT, padx=10, pady=10)

# Menambahkan menu konteks saat mengklik mouse kanan
context_menu = tk.Menu(chat_box, tearoff=0)
context_menu.add_command(label="Salin", command=copy_text, state=tk.DISABLED)
context_menu.add_command(label="Potong", command=cut_text, state=tk.DISABLED)
context_menu.add_command(label="Tempel", command=paste_text)
context_menu.add_command(label="Pilih semua", command=select_all_text)
context_menu.add_command(label="Tentang", command=show_about_window)
context_menu.add_separator()
context_menu.add_command(label="Bersihkan", command=clear_text)
context_menu.add_command(label="Setelan", command=show_settings_menu)  # Tambahkan opsi "Setelan"


def show_context_menu(event):
    if chat_box.tag_ranges(tk.SEL):
        context_menu.entryconfigure("Salin", state=tk.NORMAL)
        context_menu.entryconfigure("Potong", state=tk.NORMAL)
    else:
        context_menu.entryconfigure("Salin", state=tk.DISABLED)
        context_menu.entryconfigure("Potong", state=tk.DISABLED)
    context_menu.post(event.x_root, event.y_root)

chat_box.bind("<Button-3>", show_context_menu)
chat_box.bind("<Control-a>", select_all_text)

# Menambahkan opsi "Bersihkan" pada menu konteks
context_menu.add_separator()
context_menu.add_command(label="Bersihkan", command=clear_text)

icon_path = "icon.ico"
window.iconbitmap(default=icon_path)

app_version = "1.0.0"

# Membaca gambar ikon
icon_image = ImageTk.PhotoImage(Image.open('D:\CODING\coding\BOT\Beta DimAi\icon.ico'))

# Mengatur ikon pada jendela utama
window.iconphoto(False, icon_image)


# Menjalankan aplikasi
window.mainloop()
