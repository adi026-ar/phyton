import matplotlib.pyplot as plt
import numpy as np

# Fungsi untuk menggambar garis menggunakan Algoritma DDA
def garis_dda(x0, y0, x1, y1):
    
    # Menghitung dx dan dy
    dx = x1 - x0
    dy = y1 - y0
    
    # Menentukan jumlah step
    step = max(abs(dx), abs(dy))
    
    # Menghitung penambahan koordinat XInc dan YInc
    XInc = dx / step
    YInc = dy / step
    
    # Inisialisasi titik awal
    x = x0
    y = y0
    
    # Simpan koordinat hasil DDA
    x_points = []
    y_points = []
    
    # Loop untuk menghitung setiap titik dari garis
    for i in range(int(step) + 1):
        # Menyimpan koordinat dengan pembulatan menjadi integer
        x_points.append(int(round(x)))
        y_points.append(int(round(y)))
        
        # Menambahkan XInc dan YInc untuk mendapatkan titik berikutnya
        x += XInc
        y += YInc
        
    # Gambar garis menggunakan matplotlib
    plt.plot(x_points, y_points, marker='o', color='blue')
    plt.title('Garis dengan Algoritma DDA')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid(True)
    plt.show()

# Memanggil fungsi untuk menggambar garis dengan titik awal (2, 3) dan titik akhir (10, 8)
garis_dda(2, 3, 10, 8)