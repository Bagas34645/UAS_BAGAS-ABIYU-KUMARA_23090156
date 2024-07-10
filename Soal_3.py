# main.py

from modul_soal_3 import Queue

def main():
    queue = Queue()

    while True:
        print("\nMenu Antrian Restoran")
        print("1. Tambah Pesanan ke Antrian")
        print("2. Hapus Pesanan dari Antrian")
        print("3. Tampilkan Antrian")
        print("4. Keluar")

        choice = input("Pilih opsi (1-4): ")

        if choice == '1':
            order = input("Masukkan nama pesanan: ")
            queue.enqueue(order)
        elif choice == '2':
            queue.dequeue()
        elif choice == '3':
            queue.display()
        elif choice == '4':
            print("Terima kasih! Program selesai.")
            break
        else:
            print("Opsi tidak valid, silakan coba lagi.")

if __name__ == "__main__":
    main()
