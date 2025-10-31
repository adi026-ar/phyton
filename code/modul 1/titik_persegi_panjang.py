# Import library matplotlib untuk membuat gambar
import matplotlib.pyplot as plt

# Tentukan ukuran canvas
canvas_width = 12
canvas_height = 8

# Membuat canvas kosong dengan latar belakang putih
canvas = plt.figure(figsize=(canvas_width, canvas_height))
ax = canvas.add_subplot(111)

# Matikan axis (sumbu) untuk tampilan yang lebih bersih
ax.axis('off')

# Atur batas koordinat untuk persegi panjang
ax.set_xlim(0, 12)
ax.set_ylim(0, 8)
ax.set_aspect('equal')

# Definisikan titik-titik sudut persegi panjang
# Titik kiri bawah (sisi kiri)
x1, y1 = 2, 2
# Titik kanan bawah (sisi kanan)
x2, y2 = 10, 2
# Titik kanan atas (sisi kanan)
x3, y3 = 10, 6
# Titik kiri atas (sisi kiri)
x4, y4 = 2, 6

# Gambar titik piksel di setiap sisi dengan warna berbeda
# Sisi kiri bawah - warna merah
ax.plot(x1, y1, 'ro', markersize=15, label='Sisi Kiri Bawah (Merah)')

# Sisi kanan bawah - warna biru
ax.plot(x2, y2, 'bo', markersize=15, label='Sisi Kanan Bawah (Biru)')

# Sisi kanan atas - warna hijau
ax.plot(x3, y3, 'go', markersize=15, label='Sisi Kanan Atas (Hijau)')

# Sisi kiri atas - warna kuning
ax.plot(x4, y4, 'yo', markersize=15, label='Sisi Kiri Atas (Kuning)')

# Tambahkan judul
plt.title('Titik Piksel pada Empat Sisi Persegi Panjang', fontsize=16)

# Tambahkan legend untuk menjelaskan warna
plt.legend(loc='upper right', fontsize=10)

# Tambahkan garis tipis untuk membentuk persegi panjang (opsional)
# Garis bawah
ax.plot([x1, x2], [y1, y2], 'k--', linewidth=0.5, alpha=0.3)
# Garis kanan
ax.plot([x2, x3], [y2, y3], 'k--', linewidth=0.5, alpha=0.3)
# Garis atas
ax.plot([x3, x4], [y3, y4], 'k--', linewidth=0.5, alpha=0.3)
# Garis kiri
ax.plot([x4, x1], [y4, y1], 'k--', linewidth=0.5, alpha=0.3)

# Tampilkan gambar
plt.show()