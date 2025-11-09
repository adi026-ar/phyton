import matplotlib.pyplot as plt

# Fungsi untuk menggambar garis menggunakan algoritma DDA
def dda_algorithm(x0, y0, x1, y1):
    # Menghitung perbedaan koordinat
    dx = x1 - x0
    dy = y1 - y0
    
    # Menentukan jumlah langkah berdasarkan jarak terpanjang (step)
    steps = max(abs(dx), abs(dy))
    
    # Menyimpan titik-titik hasil algoritma DDA
    x_points = []
    y_points = []

    if steps == 0:
        x_points.append(x0)
        y_points.append(y0)
    else:
        # Menghitung perubahan x dan y per langkah
        Xinc = dx / float(steps)
        Yinc = dy / float(steps)
        
        # Inisialisasi titik awal
        x = float(x0)
        y = float(y0)
        
        # Loop untuk menghitung titik-titik sepanjang garis
        for i in range(int(steps) + 1):
            x_points.append(round(x))
            y_points.append(round(y))
            x += Xinc
            y += Yinc
            
    # Menggambar garis menggunakan matplotlib
    plt.plot(x_points, y_points, marker="o", color="b")
    plt.title(f"Garis DDA dari ({x0}, {y0}) ke ({x1}, {y1})")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(True)
    plt.show()

# Meminta input dari pengguna untuk titik awal dan titik akhir
try:
    x0 = int(input("Masukkan koordinat x0 (titik awal): "))
    y0 = int(input("Masukkan koordinat y0 (titik awal): "))
    x1 = int(input("Masukkan koordinat x1 (titik akhir): "))
    y1 = int(input("Masukkan koordinat y1 (titik akhir): "))

    # Memanggil fungsi DDA untuk menggambar garis
    dda_algorithm(x0, y0, x1, y1)
except ValueError:
    print("Input tidak valid. Harap masukkan bilangan bulat.")