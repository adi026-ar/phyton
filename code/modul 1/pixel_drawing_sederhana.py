# Import library untuk membuat gambar
import matplotlib.pyplot as plt

# Buat canvas dengan ukuran 10x10 inci
plt.figure(figsize=(10, 10))

# Buat area gambar
ax = plt.gca()

# Sembunyikan garis sumbu
ax.axis('off')

# Atur batas koordinat dari 0 sampai 10
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

# Pastikan skala x dan y sama
ax.set_aspect('equal')

# Gambar titik merah di koordinat (5, 5)
ax.plot(5, 5, 'ro', markersize=15)

# Tambahkan judul
plt.title('Titik Piksel di (5, 5)')

# Tampilkan gambar
plt.show()