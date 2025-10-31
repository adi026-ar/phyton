import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib


def gambar_mobil():
	fig, ax = plt.subplots(figsize=(6,4))

	# Body mobil (besar)
	body = patches.Rectangle((0,1), 6, 2, edgecolor='blue', facecolor='#87CEEB', linewidth=2)
	ax.add_patch(body)

	# Kabin mobil (lebih kecil di atas)
	cabin = patches.Rectangle((1.2,2.3), 3.6, 0.8, edgecolor='blue', facecolor='#B0E0E6', linewidth=2)
	ax.add_patch(cabin)

	# Roda kiri
	wheel1 = patches.Circle((1.5,0.5), 0.5, edgecolor='black', facecolor='#555555', linewidth=1.5)
	ax.add_patch(wheel1)

	# Roda kanan
	wheel2 = patches.Circle((4.5,0.5), 0.5, edgecolor='black', facecolor='#555555', linewidth=1.5)
	ax.add_patch(wheel2)

	# Set batas dan grid
	ax.set_xlim(-1,7)
	ax.set_ylim(-1,4)
	ax.set_aspect('equal', adjustable='box')
	ax.grid(True)

	# Simpan gambar
	out = r'c:\\semester 5\\grafika-komputer\\modul 2\\mobil_tugas.png'
	plt.savefig(out, bbox_inches='tight')
	print('Gambar mobil tersimpan di:', out)
	plt.show()


if __name__ == '__main__':
	gambar_mobil()

