# Fungsi untuk menginput data mahasiswa
def input_data():
    mahasiswa = {}
    while True:
        nim = input("Masukkan NIM: ")
        nama = input("Masukkan Nama: ")
        mahasiswa[nim] = nama
        
        ulang = input("Apakah ingin menginput data lagi? (y/n): ")
        if ulang.lower() != 'y':
            break
    return mahasiswa

# Fungsi untuk menampilkan data mahasiswa
def tampilkan_data(mahasiswa):
    print("\nData Mahasiswa:")
    for nim, nama in mahasiswa.items():
        print(f"NIM: {nim}, Nama: {nama}")

# Main program
if __name__ == "__main__":
    mahasiswa = input_data()
    tampilkan_data(mahasiswa)
