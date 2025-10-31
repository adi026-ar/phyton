import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Membuat sebuah figure dan axis
fig, ax = plt.subplots()

# Fungsi untuk menggambar lingkaran
def gambar_lingkaran(radius):
    """
    Menggambar lingkaran dengan radius yang ditentukan oleh parameter 'radius'.

    Parameter:
    radius (int): Radius lingkaran.
    """

    # Menggambar lingkaran dengan radius tertentu
    lingkaran = patches.Circle((0, 0), radius, edgecolor='blue', facecolor='none', linewidth=2)
    ax.add_patch(lingkaran)

    # Mengatur batas-batas tampilan sumbu agar sesuai dengan radius lingkaran
    ax.set_xlim(-radius - 10, radius + 10)
    ax.set_ylim(-radius - 10, radius + 10)

    # Menampilkan grid dan lingkaran
    plt.grid(True)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()

# Memanggil fungsi untuk menggambar lingkaran dengan radius 50 unit
gambar_lingkaran(50)