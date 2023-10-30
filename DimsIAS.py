import tkinter as tk
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import smbus

# Inisialisasi I2C bus (sesuaikan dengan perangkat Anda)
i2c_bus = smbus.SMBus(1)

# Alamat I2C sensor getaran (sesuaikan dengan perangkat Anda)
sensor_address = 0x68

# Fungsi untuk membaca data dari sensor getaran
def read_vibration_data():
    # Baca data dari sensor getaran (contoh: baca data dari register 0x00)
    data = i2c_bus.read_i2c_block_data(sensor_address, 0x00, num_bytes)
    # Lakukan pemrosesan data mentah sesuai format sensor
    # ...

    # Mengembalikan data yang telah diproses
    return processed_data

# Fungsi untuk memulai deteksi getaran
def start_detection():
    # Kode untuk memulai pengambilan data getaran secara berkala
    # ...

# Fungsi untuk menghentikan deteksi getaran
def stop_detection():
    # Kode untuk menghentikan pengambilan data getaran
    # ...

# Fungsi animasi untuk memperbarui grafik dengan data getaran terbaru
def update_graph(frame):
    vibration_data = read_vibration_data()
    # Kode untuk memperbarui grafik (misalnya, plot data getaran dalam bentuk grafik linie)
    # ...

# Membuat GUI menggunakan Tkinter
root = tk.Tk()
root.title("Deteksi Getaran")

# Tombol untuk memulai dan menghentikan deteksi getaran
start_button = tk.Button(root, text="Mulai Deteksi", command=start_detection)
stop_button = tk.Button(root, text="Hentikan Deteksi", command=stop_detection)
start_button.pack()
stop_button.pack()

# Membuat grafik menggunakan Matplotlib
fig = plt.figure()
graph = fig.add_subplot(1, 1, 1)
ani = animation.FuncAnimation(fig, update_graph, interval=1000)  # Refresh grafik setiap 1000 ms (1 detik)

# Jalankan GUI loop
root.mainloop()
