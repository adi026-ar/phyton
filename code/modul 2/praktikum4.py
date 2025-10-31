import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Membuat sebuah figure dan axis
fig, ax = plt.subplots()

# Fungsi untuk menggambar persegi panjang
def gambar_persegi_panjang(lebar, tinggi):
    """
    Menggambar persegi panjang dengan lebar dan tinggi yang ditentukan.

    Parameter:
    lebar (int): Lebar persegi panjang.
    tinggi (int): Tinggi persegi panjang.
    """

    # Membuat objek persegi panjang dengan lebar dan tinggi tertentu
    persegi_panjang = patches.Rectangle((0, 0), lebar, tinggi, edgecolor='blue', facecolor='none', linewidth=2)
    ax.add_patch(persegi_panjang)

    # Mengatur batas-batas tampilan sumbu agar sesuai dengan ukuran persegi panjang
    ax.set_xlim(-10, lebar + 10)
    ax.set_ylim(-10, tinggi + 10)

    # Menampilkan grid dan persegi panjang
    plt.grid(True)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()

# Memanggil fungsi untuk menggambar persegi panjang dengan lebar 100 unit dan tinggi 50 unit
gambar_persegi_panjang(100, 50)