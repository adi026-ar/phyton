"""tugasDDA.py
Perbaikan dan penambahan fitur untuk implementasi algoritma DDA.

Fitur tambahan:
- Parsing input yang lebih aman (via argparse atau input interaktif)
- Normalisasi arah (A ke B atau B ke A)
- Fungsi terpisah `dda_points` yang mengembalikan koordinat (float dan integer/rounded)
- Opsi menyimpan plot ke file (`--save`) sehingga dapat dijalankan headless

Usage examples:
  python tugasDDA.py            # interactive mode
  python tugasDDA.py --xa 1 --ya 1 --xb 6 --yb 3 --direction "A ke B" --save out.png
"""

import argparse
import math
import matplotlib
import matplotlib.pyplot as plt
import sys
from typing import List, Tuple


def dda_points(x0: float, y0: float, x1: float, y1: float) -> Tuple[List[float], List[float], List[int], List[int]]:
    """Hitung titik-titik dengan algoritma DDA.

    Returns:
        xs_f, ys_f: lists of float coordinates (line path)
        xs_i, ys_i: lists of rounded integer coordinates (DDA pixel positions)
    """
    dx = x1 - x0
    dy = y1 - y0
    steps = int(max(abs(dx), abs(dy)))

    # Jika dx dan dy kurang dari 1 tetapi tidak nol, pastikan minimal 1 langkah
    if steps == 0:
        x_inc = 0.0
        y_inc = 0.0
    else:
        x_inc = dx / steps
        y_inc = dy / steps

    x = x0
    y = y0
    xs_f = []
    ys_f = []
    xs_i = []
    ys_i = []
    for _ in range(steps + 1):
        xs_f.append(x)
        ys_f.append(y)
        xs_i.append(int(round(x)))
        ys_i.append(int(round(y)))
        x += x_inc
        y += y_inc

    return xs_f, ys_f, xs_i, ys_i


def normalize_direction(direction: str) -> str:
    s = (direction or '').strip().lower()
    # keep only alphanumeric characters to simplify matching
    s2 = ''.join(ch for ch in s if ch.isalnum())
    if not s2:
        return 'a->b'
    # if starts with b and contains a later -> B to A
    if s2.startswith('b') and 'a' in s2[1:]:
        return 'b->a'
    if s2.startswith('a') and 'b' in s2[1:]:
        return 'a->b'
    # fallback: explicit keywords
    if 'btoa' in s2 or 'b2a' in s2:
        return 'b->a'
    if 'atob' in s2 or 'a2b' in s2:
        return 'a->b'
    return 'a->b'


def parse_args():
    p = argparse.ArgumentParser(description='Implementasi algoritma DDA (Digital Differential Analyzer)')
    p.add_argument('--xa', type=float, help='Koordinat x titik A')
    p.add_argument('--ya', type=float, help='Koordinat y titik A')
    p.add_argument('--xb', type=float, help='Koordinat x titik B')
    p.add_argument('--yb', type=float, help='Koordinat y titik B')
    p.add_argument('--direction', type=str, default='A ke B', help='Arah penggambaran (contoh: "A ke B" atau "B ke A")')
    p.add_argument('--save', nargs='?', const='tugasDDA_output.png', help='Jika diberikan, simpan plot ke file (opsional: berikan nama file)')
    return p.parse_args()


def main():
    args = parse_args()

    # Input: gunakan argumen CLI bila tersedia, sebaliknya minta input interaktif
    try:
        if args.xa is None:
            print('--- Input Titik ---')
            xa = float(input('Masukkan koordinat x untuk Titik A: '))
            ya = float(input('Masukkan koordinat y untuk Titik A: '))
            xb = float(input('Masukkan koordinat x untuk Titik B: '))
            yb = float(input('Masukkan koordinat y untuk Titik B: '))
        else:
            xa, ya, xb, yb = args.xa, args.ya, args.xb, args.yb
    except Exception as e:
        print('Input tidak valid:', e)
        return

    dir_norm = normalize_direction(args.direction)
    if dir_norm == 'b->a':
        x0, y0, x1, y1 = xb, yb, xa, ya
        dir_label = 'B -> A'
    else:
        x0, y0, x1, y1 = xa, ya, xb, yb
        dir_label = 'A -> B'

    print('\n--- Algoritma DDA ---')
    xs_f, ys_f, xs_i, ys_i = dda_points(x0, y0, x1, y1)

    print('Koordinat (rounded) yang dihitung:')
    for xi, yi in zip(xs_i, ys_i):
        print(f'({xi}, {yi})')

    # Gambar hasil
    # Jika user meminta penyimpanan, pakai backend non-interaktif
    savefile = args.save
    if savefile:
        matplotlib.use('Agg')

    fig, ax = plt.subplots()
    # plot garis (float) untuk visual hasil DDA
    ax.plot(xs_f, ys_f, marker='o', linestyle='-', color='blue', label=f'Garis ({dir_label})')
    # tambahkan titik integer (hasil rounding) sebagai marker merah
    ax.scatter(xs_i, ys_i, color='red', s=30, label='Titik DDA (rounded)')

    ax.set_title('Implementasi Algoritma DDA')
    ax.set_xlabel('Sumbu X')
    ax.set_ylabel('Sumbu Y')
    ax.grid(True)
    ax.legend()
    ax.axis('equal')

    if savefile:
        print(f'Menyimpan plot ke: {savefile}')
        plt.savefig(savefile, bbox_inches='tight')
    else:
        plt.show()


if __name__ == '__main__':
    main()