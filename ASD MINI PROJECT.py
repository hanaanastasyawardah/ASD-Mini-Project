from prettytable import PrettyTable
import os

class TokoOlahraga:
    def __init__(self):
        self.perlengkapan = {}

    def tambah_perlengkapan(self, nama, jenis, harga, jumlah):
        self.perlengkapan[nama] = {'jenis': jenis, 'harga': harga, 'jumlah': jumlah}
        print("Perlengkapan berhasil ditambahkan.")

    def lihat_perlengkapan(self):
        try:
            if self.perlengkapan:
                while True:
                    table = PrettyTable(["Nama", "Jenis", "Harga", "Jumlah"])
                    for nama, data in self.perlengkapan.items():
                        table.add_row([nama, data['jenis'], data['harga'], data['jumlah']])
                    print("Daftar Perlengkapan Olahraga:")
                    print(table)
                    if input("Tekan 'q' untuk keluar: ").lower() == 'q':
                        break
            else:
                print("Perlengkapan olahraga tidak ada yang terdaftar.")
        except Exception as e:
            print(f"Error: {e}")

    def cari_perlengkapan(self, nama):
        try:
            if nama in self.perlengkapan:
                while True:
                    data = self.perlengkapan[nama]
                    table = PrettyTable(["Detail Perlengkapan", "Nilai"])
                    for key, value in data.items():
                        table.add_row([key, value])
                    print("Detail Perlengkapan:")
                    print(table)
                    if input("Tekan 'q' untuk keluar: ").lower() == 'q':
                        break
            else:
                print("Perlengkapan tidak ditemukan.")
        except Exception as e:
            print(f"Error: {e}")

    def update_perlengkapan(self, nama, jenis, harga, jumlah):
        try:
            if nama in self.perlengkapan:
                self.perlengkapan[nama] = {'jenis': jenis, 'harga': harga, 'jumlah': jumlah}
                print("Perlengkapan berhasil diupdate.")
            else:
                print("Perlengkapan tidak ditemukan.")
        except Exception as e:
            print(f"Error: {e}")

    def hapus_perlengkapan(self, nama):
        try:
            if nama in self.perlengkapan:
                del self.perlengkapan[nama]
                print("Perlengkapan berhasil dihapus.")
            else:
                print("Perlengkapan tidak ditemukan.")
        except Exception as e:
            print(f"Error: {e}")

def main():
    toko = TokoOlahraga()

    daftar_peralatan = [
        ("Sepatu Lari", "Sepatu", 250000, 10),
        ("Bola Basket", "Bola", 150000, 20),
        ("Raket Tennis", "Raket", 200000, 15),
        ("Baju Renang", "Pakaian", 100000, 25),
        ("Sarung Tinju", "Alat Tinju", 300000, 5),
        ("Trampolin", "Alat Pelatihan", 100000, 15),
        ("Papan Selancar", "Perlengkapan Selancar", 500000, 3),
        ("Treadmill", "Alat Olahraga Elektronik", 2000000, 2),
        ("Raket Bulutangkis", "Raket", 150000, 12),
        ("Jersey Basket", "Pakaian", 120000, 15)
    ]

    for peralatan in daftar_peralatan:
        toko.tambah_perlengkapan(*peralatan)

    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print("\n🌺=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+🌺")
        print("🌼                                                        🌼")
        print("💐                    PINK VELVET ATHLETICS               💐")
        print("🌼                                                        🌼")
        print("🌺=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+🌺")
        print("1. LIHAT PERLENGKAPAN                                     🌼")
        print("2. CARI PERLENGKAPAN                                      💐")
        print("3. UPDATE PERLENGKAPAN                                    🌼")
        print("4. HAPUS PERLENGKAPAN                                     💐")
        print("5. EXIT                                                   🌼")
        print("🌺=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+🌺")

        pilihan = input("Masukkan pilihan Anda: ")

        if pilihan == "1":
            toko.lihat_perlengkapan()
        elif pilihan == "2":
            nama = input("Masukkan nama perlengkapan: ")
            toko.cari_perlengkapan(nama)
        elif pilihan == "3":
            nama = input("Masukkan nama perlengkapan yang ingin diupdate: ")
            jenis = input("Jenis: ")
            harga = int(input("Harga: "))
            jumlah = int(input("Jumlah: "))
            toko.update_perlengkapan(nama, jenis, harga, jumlah)
        elif pilihan == "4":
            nama = input("Masukkan nama perlengkapan yang ingin dihapus: ")
            toko.hapus_perlengkapan(nama)
        elif pilihan == "5":
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("🌻💐🌷                                                                          🌻💐🌷")
            print("🌸🌼🌺       Terima kasih telah menggunakan layanan Pink Velvet Athletics!      🌸🌼🌺")
            print("🏊‍♀️⛹️‍♂️🏋️‍♀️                                                                          🏊‍♀️⛹️‍♂️🏋️‍♀️")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih menu yang sesuai.")

if __name__ == "__main__":
    main()
