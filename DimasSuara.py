import speech_recognition as sr
import pyttsx3
import random
import re

# Inisialisasi objek SpeechRecognition
recognizer = sr.Recognizer()

# Inisialisasi objek pyttsx3
engine = pyttsx3.init()

def listen_for_command():
    with sr.Microphone() as source:
        print("Mendengar...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("merangkap...")
        command = recognizer.recognize_google(audio)
        print("Kamu Ucap:", command)

        response = generate_response(command)
        speak(response)
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand what you said.")
    except sr.RequestError as e:
        print("Galat:", str(e))

def generate_response(question):
    if any(word in question.lower() for word in ["halo", "hai", "oi", "hi"]):
        return "Halo! Ada yang bisa saya bantu?"
    elif "siapa nama kamu" in question.lower():
        return "Saya adalah DimasAI, Dikembangkan oleh anak SMA yaitu Raihan dari SMA 15 Kota Tangerang"
    elif "apa kabar" in question.lower():
        return "Saya adalah AI, jadi saya tidak memiliki perasaan. Tapi terima kasih telah bertanya!"
    elif "terima kasih" in question.lower():
        return "Sama-sama, senang bisa membantu!"
    elif "apakah kamu manusia" in question.lower():
        return "Tidak, saya adalah program komputer yang dikembangkan oleh INDESU."
    elif any(word in question.lower() for word in ["ngewe", "kontl", "kontol", "anjing", "bego"]):
        return "Maaf, pertanyaan tersebut tidak pantas dan tidak relevan."
    elif "apa hobi kamu" in question.lower():
        return "Sebagai AI, saya tidak memiliki hobi seperti manusia. Saya dirancang untuk membantu menjawab pertanyaan."
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
    elif "buatlah kode contoh html" in question.lower() or "contoh kode html" in question.lower() or "buat kode html" in question.lower():
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
    elif "buka aplikasi" in question.lower():
        app_name = re.findall(r"buka aplikasi (.+)", question.lower())[0]

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

def speak(text):
    engine.say(text)
    engine.runAndWait()

def exit_program():
    speak("Selamat tinggal!")
    exit()

# Mulai mendengarkan perintah
while True:
    listen_for_command()
