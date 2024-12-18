import matplotlib.pyplot as plt
import numpy as np

# Data yang diambil dari grafik
categories = [
    'Penalaran Deduktif', 
    'Pengetahuan Kuantitatif', 
    'Pemahaman Bacaan & Menulis', 
    'Literasi Bahasa Inggris', 
    'Penalaran Kuantitatif'
]

nilai_siswa = [700, 500, 1200, 400, 600]
rata_rata_nasional = [800, 600, 1100, 500, 700]

# Tentukan posisi bar di grafik
bar_width = 0.35  # Lebar batang
index = np.arange(len(categories))  # Lokasi batang

# Membuat plot
fig, ax = plt.subplots()

# Plot batang untuk nilai siswa
bar1 = ax.barh(index, nilai_siswa, bar_width, label='Nilai Siswa', color='blue')

# Plot batang untuk rata-rata nasional
bar2 = ax.barh(index + bar_width, rata_rata_nasional, bar_width, label='Rata-Rata Nasional', color='orange')

# Menambahkan label dan judul
ax.set_xlabel('Nilai')
ax.set_title('Perbandingan Nilai Siswa dengan Rata-Rata Sekolah')
ax.set_yticks(index + bar_width / 2)
ax.set_yticklabels(categories)

# Menambahkan legenda
ax.legend()

# Tampilkan grafik
plt.show()
