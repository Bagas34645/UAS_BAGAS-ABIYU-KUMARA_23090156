# Kelas parent: Buah
class Buah:
    def __init__(self, nama="", warna="", rasa=""):
        self.nama = nama
        self.warna = warna
        self.rasa = rasa

    def setNama(self, nama):
        self.nama = nama

    def setWarna(self, warna):
        self.warna = warna

    def setRasa(self, rasa):
        self.rasa = rasa

    def Information(self):
        return f"Nama: {self.nama}, Warna: {self.warna}, Rasa: {self.rasa}"

# Kelas child: Mangga yang mewarisi dari Buah
class Mangga(Buah):
    def __init__(self, nama="", warna="", rasa="", vitamin=""):
        super().__init__(nama, warna, rasa)
        self.vitamin = vitamin

    def setVitamin(self, vitamin):
        self.vitamin = vitamin

    def information(self):
        parent_info = super().Information()
        return f"{parent_info}, Vitamin: {self.vitamin}"

# Membuat instance objek dari kelas Mangga
mangga1 = Mangga()
mangga1.setNama("Mangga Harum Manis")
mangga1.setWarna("Hijau Kekuningan")
mangga1.setRasa("Manis")
mangga1.setVitamin("Vitamin C")

# Memanggil atribut dan metode
print(mangga1.information())
