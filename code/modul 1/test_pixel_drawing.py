import matplotlib.pyplot as plt

# Tentukan ukuran canvas
canvas_width = 10
canvas_height = 10

# Membuat canvas kosong dengan latar belakang putih
canvas = plt.figure(figsize=(canvas_width, canvas_height))
ax = canvas.add_subplot(111)

# Matikan axis (sumbu)
ax.axis('off')

# Atur batas koordinat untuk memastikan titik terlihat jelas
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.set_aspect('equal')

# Gambar titik piksel di koordinat (5, 5)
ax.plot(5, 5, 'ro', markersize=10)  # 'ro' berarti titik merah bulat

# Tambahkan judul
plt.title('Gambar Titik Piksel di Koordinat (5, 5)', fontsize=14)

# Tampilkan gambar
plt.show()