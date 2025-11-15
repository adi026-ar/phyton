import matplotlib.pyplot as plt

def midpoint_circle(h, k, r):
    x = 0
    y = r
    points = []
    
    # Parameter keputusan
    p = 1 - r
    
    # Helper function to add symmetric points
    def add_symmetric_points(h, k, x, y):
        # Menambahkan titik dari simetri, menggunakan set untuk menghindari duplikat
        points.extend(list(set([
            (h + x, k + y),
            (h - x, k + y),
            (h + x, k - y),
            (h - x, k - y),
            (h + y, k + x),
            (h - y, k + x),
            (h + y, k - x),
            (h - y, k - x)
        ])))

    # Menggambar titik awal di delapan oktan
    add_symmetric_points(h, k, x, y)
    
    while x < y:
        x += 1
        if p < 0:
            p += 2 * x + 1
        else:
            y -= 1
            p += 2 * (x - y) + 1
            
        # Menambahkan titik dari simetri
        add_symmetric_points(h, k, x, y)
        
    return points

# Parameter lingkaran
center_x = 0
center_y = 0
radius = 10

# Menggambar lingkaran
circle_points = midpoint_circle(center_x, center_y, radius)

# Menyiapkan plot
plt.figure(figsize=(8, 8))

# Ekstrak koordinat x dan y untuk plotting yang efisien
x_coords = [point[0] for point in circle_points]
y_coords = [point[1] for point in circle_points]

plt.plot(x_coords, y_coords, 'bo') # Menggambar semua titik sekaligus

plt.title('Lingkaran menggunakan Algoritma Midpoint Circle')
plt.xlim(-radius - 1, radius + 1)
plt.ylim(-radius - 1, radius + 1)
plt.axhline(0, color='black', linewidth=0.5, ls='--')
plt.axvline(0, color='black', linewidth=0.5, ls='--')
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
plt.gca().set_aspect('equal', adjustable='box')
plt.show()
