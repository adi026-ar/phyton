import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Membuat sebuah figure dan axis
fig, ax = plt.subplots()

# Fungsi untuk menggambar segitiga
def gambar_segitiga(panjang_sisi):
    
    # Menghitung koordinat titik-titik segitiga
    t1 = (0, 0)
    t2 = (panjang_sisi, 0)
    t3 = (panjang_sisi / 2, (panjang_sisi * (3 ** 0.5)) / 2) # Tinggi segitiga sama sisi

    # Membuat objek segitiga dengan koordinat yang dihitung
    segitiga = patches.Polygon([t1, t2, t3], closed=True, edgecolor='blue', facecolor='none', linewidth=2)
    ax.add_patch(segitiga)

    # Mengatur batas-batas tampilan sumbu agar sesuai dengan ukuran segitiga
    ax.set_xlim(-10, panjang_sisi + 10)
    ax.set_ylim(-10, (panjang_sisi * (3 ** 0.5)) / 2 + 10)

    # Menampilkan grid dan segitiga
    plt.grid(True)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()

# Memanggil fungsi untuk menggambar segitiga dengan panjang sisi 100 unit
gambar_segitiga(100)