import numpy as py
import pandas as pd

# Fungsi untuk menyimpan data siswa ke file Excel
def simpan_data_siswa_ke_excel(nama_file, data_siswa):
    # Membuat workbook dan menambah data ke sheet
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.title = "Data Siswa"

    # Membuat header
    headers = ["Nama", "User ID", "Email", "Nilai Penalaran Kuantitatif", "Nilai Pengetahuan Umum", "Rata-rata"]
    sheet.append(headers)

    # Menambahkan data siswa ke dalam sheet
    sheet.append(data_siswa)

    # Menyimpan file Excel
    workbook.save(nama_file)
    print(f"Data untuk {data_siswa[0]} berhasil disimpan ke {nama_file}")

# Fungsi untuk memproses dataset dari Excel dan membuat file excel untuk tiap siswa
def olah_dataset(file_excel):
    # Membaca dataset dari file Excel
    df = pd.read_excel(file_excel)

    # Iterasi untuk setiap record siswa di dataset
    for index, row in df.iterrows():
        # Membuat nama file berdasarkan nama siswa dan user_id
        nama_siswa = row['Nama']
        user_id = row['User_id']
        nama_file = f"{nama_siswa}_{user_id}.xlsx"
        
        # Data siswa (sesuai urutan header)
        data_siswa = [
            row['Nama'],
            row['User_id'],
            row['Email'],
            row['Nilai Penalaran Kuantitatif'],
            row['Nilai Pengetahuan Umum'],
            row['Rata-rata']
        ]
        
        # Simpan data ke dalam file Excel
        simpan_data_siswa_ke_excel(nama_file, data_siswa)

# Contoh penggunaan
file_excel = "dataset_tryout_snbt.xlsx"  # Nama file Excel yang berisi data siswa
olah_dataset(file_excel)

