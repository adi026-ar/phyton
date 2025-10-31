# Import library untuk membuat gambar
import matplotlib.pyplot as plt
import numpy as np

# Buat canvas dengan ukuran 10x10 inci
plt.figure(figsize=(10, 10))

# Buat area gambar
ax = plt.gca()

# Sembunyikan garis sumbu
ax.axis('off')

# Atur batas koordinat agar segitiga terlihat jelas
ax.set_xlim(-1, 11)
ax.set_ylim(-1, 11)

# Pastikan skala x dan y sama
ax.set_aspect('equal')

# Definisikan titik-titik segitiga dengan sisi 10
# Titik A di (5, 8.66) - puncak segitiga
# Titik B di (0, 0) - kiri bawah
# Titik C di (10, 0) - kanan bawah
# Tinggi segitiga = 10 * sqrt(3) / 2 = 8.66
tinggi = 10 * np.sqrt(3) / 2

# Koordinat titik-titik segitiga
x_points = [5, 0, 10, 5]  # kembali ke titik awal untuk menutup segitiga
y_points = [tinggi, 0, 0, tinggi]

# Gambar segitiga dengan garis merah
ax.plot(x_points, y_points, 'r-', linewidth=3)

# Tambahkan judul
plt.title('Segitiga dengan Warna Garis Merah - Panjang Sisi 10')

# Tampilkan gambar
plt.show()