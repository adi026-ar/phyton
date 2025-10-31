# Import library untuk membuat gambar
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Buat canvas dengan ukuran 10x10 inci
plt.figure(figsize=(10, 10))

# Buat area gambar
ax = plt.gca()

# Sembunyikan garis sumbu
ax.axis('off')

# Atur batas koordinat agar persegi panjang terlihat jelas
ax.set_xlim(-1, 15)
ax.set_ylim(-1, 10)

# Pastikan skala x dan y sama
ax.set_aspect('equal')

# Buat persegi panjang pertama (horizontal)
# Posisi: (1, 4), Ukuran: lebar=6, tinggi=3
rect1 = patches.Rectangle((1, 4), 6, 3, linewidth=2, edgecolor='blue', facecolor='none')

# Buat persegi panjang kedua (vertikal) yang menyatu dengan yang pertama
# Posisi: (6, 1), Ukuran: lebar=3, tinggi=6
rect2 = patches.Rectangle((6, 1), 3, 6, linewidth=2, edgecolor='red', facecolor='none')

# Tambahkan persegi panjang ke dalam gambar
ax.add_patch(rect1)
ax.add_patch(rect2)

# Tambahkan titik sudut untuk memperjelas pertemuan
ax.plot(6, 4, 'ko', markersize=8)

# Tambahkan judul
plt.title('Dua Persegi Panjang yang Saling Menyatu')

# Tampilkan gambar
plt.show()