# Import library matplotlib untuk membuat grafik dan gambar
import matplotlib.pyplot as plt

# Tentukan lebar canvas (dalam inci) untuk tampilan gambar
canvas_width = 10

# Tentukan tinggi canvas (dalam inci) untuk tampilan gambar
canvas_height = 10

# Membuat objek figure (canvas) kosong dengan ukuran yang ditentukan
# figsize=(width, height) menentukan ukuran canvas dalam inci
canvas = plt.figure(figsize=(canvas_width, canvas_height))

# Menambahkan subplot (area gambar) ke dalam canvas
# 111 berarti 1 baris, 1 kolom, subplot ke-1
ax = canvas.add_subplot(111)

# Mematikan tampilan sumbu koordinat (axis) untuk tampilan yang lebih bersih
ax.axis('off')

# Mengatur batas koordinat sumbu X dari 0 sampai 10
# Ini memastikan area gambar mencakup koordinat (5,5) dengan baik
ax.set_xlim(0, 10)

# Mengatur batas koordinat sumbu Y dari 0 sampai 10
# Ini memastikan area gambar mencakup koordinat (5,5) dengan baik
ax.set_ylim(0, 10)

# Mengatur rasio aspek agar sama antara sumbu X dan Y
# Ini memastikan lingkaran tidak menjadi elips
ax.set_aspect('equal')

# Menggambar titik piksel di koordinat (5, 5)
# 'ro' berarti titik merah (red) bulat (circle)
# markersize=10 menentukan ukuran titik
ax.plot(5, 5, 'ro', markersize=10)

# Menambahkan judul pada gambar
# fontsize=14 menentukan ukuran huruf judul
plt.title('Gambar Titik Piksel di Koordinat (5, 5)', fontsize=14)

# Menampilkan gambar yang telah dibuat
# Fungsi ini akan membuka window baru dengan gambar
plt.show()