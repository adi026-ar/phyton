import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Membuat sebuah figure dan axis
fig, ax = plt.subplots()

# Fungsi untuk menggambar kotak
def gambar_kotak(ukuran):
    """
    Menggambar kotak dengan panjang sisi yang ditentukan oleh parameter 'ukuran'.

    Parameter:
    ukuran (int): Panjang sisi kotak.
    """

    # Menggambar persegi dengan ukuran tertentu
    kotak = patches.Rectangle((0, 0), ukuran, ukuran, edgecolor='blue', facecolor='none', linewidth=2)
    ax.add_patch(kotak)

    # Mengatur batas-batas tampilan sumbu agar sesuai dengan ukuran kotak
    ax.set_xlim(-10, ukuran + 10)
    ax.set_ylim(-10, ukuran + 10)

    # Menampilkan grid dan kotak
    plt.grid(True)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()

# Memanggil fungsi untuk menggambar kotak dengan ukuran sisi 100 unit
gambar_kotak(100)