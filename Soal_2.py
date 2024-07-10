import pandas as pd

# Data Mahasiswa dan Nilai
data = {
    "Nama": ["Mahasiswa 1", "Mahasiswa 2", "Mahasiswa 3"],
    "Algoritma dan Struktur Data 2": [90, 50, 65],
    "Matematika Numerik": [80, 60, 70]
}

# Membuat DataFrame
df = pd.DataFrame(data)

# Menampilkan DataFrame
print("Data Mahasiswa dan Nilai:")
print(df)

# Menghitung rata-rata nilai untuk setiap mata kuliah
rata_rata_mata_kuliah = df.mean(axis=0, numeric_only=True)
print("\nRata-rata Nilai untuk Setiap Mata Kuliah:")
print(rata_rata_mata_kuliah)

# Menghitung rata-rata nilai untuk setiap mahasiswa
rata_rata_mahasiswa = df.mean(axis=1, numeric_only=True)
df["Rata-rata"] = rata_rata_mahasiswa
print("\nRata-rata Nilai untuk Setiap Mahasiswa:")
print(df[["Nama", "Rata-rata"]])
