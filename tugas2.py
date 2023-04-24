class AntrianHaji:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def tambah_antrian(self, nama, kota_kelahiran):
        self.items.append({"nama": nama, "kota_kelahiran": kota_kelahiran})

    def keluar_antrian(self):
        if self.is_empty():
            print("Antrian Kosong")
        else:
            antrian = self.items.pop(0)
            print(f"Keluar antrian: {antrian['nama']}, {antrian['kota_kelahiran']}")

    def tampilkan_antrian(self):
        if self.is_empty():
            print("Antrian Kosong")
        else:
            print("Daftar Antrian:")
            for i, item in enumerate(self.items):
                print(f"{i+1}. {item['nama']}, {item['kota_kelahiran']}")

if __name__ == '__main__':
    antrian_haji = AntrianHaji()

    while True:
        print("1. Daftar Antrian")
        print("2. Keluar Antrian")
        print("3. Tampilkan Antrian")
        print("4. Keluar Program")
        pilihan = int(input("Masukkan Pilihan: "))

        if pilihan == 1:
            nama = input("Masukkan Nama: ")
            kota_kelahiran = input("Masukkan Kota Kelahiran: ")
            antrian_haji.tambah_antrian(nama, kota_kelahiran)
            print("Berhasil ditambahkan ke antrian")

        elif pilihan == 2:
            antrian_haji.keluar_antrian()

        elif pilihan == 3:
            antrian_haji.tampilkan_antrian()

        elif pilihan == 4:
            break

        else:
            print("Pilihan tidak valid")