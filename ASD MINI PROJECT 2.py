from os import system
import os
from prettytable import PrettyTable

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def tambah_di_awal(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def tambah_di_akhir(self, data):
        if not self.head:
            self.head = Node(data)
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = Node(data)

    def tambah_di_antara(self, posisi, data):
        if posisi < 0:
            print("Posisi tidak valid.")
            return
        if posisi == 0:
            self.tambah_di_awal(data)
            return
        new_node = Node(data)
        current = self.head
        for _ in range(posisi - 1):
            if current is None:
                print("Posisi melebihi jumlah node.")
                return
            current = current.next
        if current is None:
            print("Posisi melebihi jumlah node.")
            return
        new_node.next = current.next
        current.next = new_node

    def hapus_di_awal(self):
        if not self.head:
            print("Linked list sudah kosong.")
            return
        self.head = self.head.next

    def hapus_di_akhir(self):
        if not self.head:
            print("Linked list sudah kosong.")
            return
        if self.head.next is None:
            self.head = None
            return
        current = self.head
        while current.next.next:
            current = current.next
        current.next = None

    def hapus_di_antara(self, posisi):
        if posisi < 0 or not self.head:
            print("Posisi tidak valid atau linked list kosong.")
            return
        if posisi == 0:
            self.hapus_di_awal()
            return
        current = self.head
        for _ in range(posisi - 1):
            if current.next is None:
                print("Posisi melebihi jumlah node.")
                return
            current = current.next
        if current.next is None:
            print("Posisi melebihi jumlah node.")
            return
        current.next = current.next.next

    def cetak_linked_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

class TokoOlahraga:
    def __init__(self):
        self.perlengkapan = LinkedList()

    def tambah_perlengkapan(self, data):
        if data:
            self.perlengkapan.tambah_di_akhir(data)
            print("Perlengkapan berhasil ditambahkan.")
        else:
            print("Data perlengkapan tidak valid.")

    def tambah_perlengkapan_awal(self, data):
        if data:
            self.perlengkapan.tambah_di_awal(data)
            print("Perlengkapan berhasil ditambahkan di awal.")
        else:
            print("Data perlengkapan tidak valid.")

    def tambah_perlengkapan_tengah(self, posisi, data):
        if data:
            self.perlengkapan.tambah_di_antara(posisi, data)
            print("Perlengkapan berhasil ditambahkan di tengah.")
        else:
            print("Data perlengkapan tidak valid.")

    def tambah_perlengkapan_akhir(self, data):
        if data:
            self.perlengkapan.tambah_di_akhir(data)
            print("Perlengkapan berhasil ditambahkan di akhir.")
        else:
            print("Data perlengkapan tidak valid.")

    def lihat_perlengkapan(self):
        if self.perlengkapan.head:
            table = PrettyTable(["Nama", "Jenis", "Harga", "Jumlah"])
            table.align["Nama"] = "l"
            table.align["Jenis"] = "l"
            table.align["Harga"] = "r"
            table.align["Jumlah"] = "r"
            current = self.perlengkapan.head
            while current:
                harga_formatted = f"Rp {current.data['Harga']:,}"
                jumlah_formatted = f"{current.data['Jumlah']:,}"
                table.add_row([current.data['Nama'], current.data['Jenis'], harga_formatted, jumlah_formatted])
                current = current.next
            print("Daftar Perlengkapan Olahraga:")
            print(table)
        else:
            print("Daftar Perlengkapan Olahraga masih kosong.")

    def cari_perlengkapan(self, nama):
        current = self.perlengkapan.head
        while current:
            if current.data['Nama'] == nama:
                print("Detail Perlengkapan:")
                print(current.data)
                break
            current = current.next
        else:
            print("Perlengkapan tidak ditemukan.")

    def update_perlengkapan(self, nama, jenis, harga, jumlah):
        current = self.perlengkapan.head
        while current:
            if current.data['Nama'] == nama:
                current.data = {'Nama': nama, 'Jenis': jenis, 'Harga': harga, 'Jumlah': jumlah}
                print("Perlengkapan berhasil diupdate.")
                break
            current = current.next
        else:
            print("Perlengkapan tidak ditemukan.")

    def hapus_perlengkapan(self, nama):
        current = self.perlengkapan.head
        prev = None
    
        while current:
            if current.data['Nama'] == nama:
                if prev is None:
                    self.perlengkapan.hapus_di_awal()
                else:
                    prev.next = current.next
                print("Perlengkapan berhasil dihapus.")
                break
            prev = current
            current = current.next
        else:
            print("Perlengkapan tidak ditemukan.")


def main():
    toko = TokoOlahraga()

    daftar_peralatan = [
        {"Nama": "Sepatu Lari", "Jenis": "Sepatu", "Harga": 250000, "Jumlah": 10},
        {"Nama": "Bola Basket", "Jenis": "Bola", "Harga": 150000, "Jumlah": 20},
        {"Nama": "Raket Tennis", "Jenis": "Raket", "Harga": 200000, "Jumlah": 15},
        {"Nama": "Baju Renang", "Jenis": "Pakaian", "Harga": 100000, "Jumlah": 25},
        {"Nama": "Sarung Tinju", "Jenis": "Alat Tinju", "Harga": 300000, "Jumlah": 5},
        {"Nama": "Trampolin", "Jenis": "Alat Pelatihan", "Harga": 100000, "Jumlah": 15},
        {"Nama": "Papan Selancar", "Jenis": "Perlengkapan Selancar", "Harga": 500000, "Jumlah": 3},
        {"Nama": "Treadmill", "Jenis": "Alat Olahraga Elektronik", "Harga": 2000000, "Jumlah": 2},
        {"Nama": "Raket Bulutangkis", "Jenis": "Raket", "Harga": 150000, "Jumlah": 12},
        {"Nama": "Jersey Basket", "Jenis": "Pakaian", "Harga": 120000, "Jumlah": 15}
    ]

    for peralatan in daftar_peralatan:
        toko.tambah_perlengkapan(peralatan)

    while True:
        os.system("cls")
        print("\n🌺=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+🌺")
        print("🌼                                                        🌼")
        print("💐                    PINK VELVET ATHLETICS               💐")
        print("🌼                                                        🌼")
        print("🌺=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+🌺")
        print("1. TAMBAH PERLENGKAPAN                                     🌼")
        print("2. LIHAT PERLENGKAPAN                                      💐")
        print("3. CARI PERLENGKAPAN                                       🌼")
        print("4. UPDATE PERLENGKAPAN                                     💐")
        print("5. HAPUS PERLENGKAPAN                                      🌼")
        print("6. EXIT                                                    💐")
        print("🌺=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+🌺")

        pilihan = input("Masukkan pilihan Anda: ")

        if pilihan == "1":
            print("\n1. TAMBAH PERLENGKAPAN DI AWAL")
            print("2. TAMBAH PERLENGKAPAN DI TENGAH")
            print("3. TAMBAH PERLENGKAPAN DI AKHIR")
            pilihan_tambah = input("Pilih jenis penambahan perlengkapan: ")
            if pilihan_tambah == "1":
                data = {
                    "Nama": input("Nama: "),
                    "Jenis": input("Jenis: "),
                    "Harga": int(input("Harga: ")),
                    "Jumlah": int(input("Jumlah: "))
                }
                toko.tambah_perlengkapan_awal(data)
            elif pilihan_tambah == "2":
                posisi = int(input("Posisi: "))
                data = {
                    "Nama": input("Nama: "),
                    "Jenis": input("Jenis: "),
                    "Harga": int(input("Harga: ")),
                    "Jumlah": int(input("Jumlah: "))
                }
                toko.tambah_perlengkapan_tengah(posisi, data)
            elif pilihan_tambah == "3":
                data = {
                    "Nama": input("Nama: "),
                    "Jenis": input("Jenis: "),
                    "Harga": int(input("Harga: ")),
                    "Jumlah": int(input("Jumlah: "))
                }
                toko.tambah_perlengkapan_akhir(data)
            else:
                print("Pilihan tidak valid.")
        elif pilihan == "2":
            toko.lihat_perlengkapan()
        elif pilihan == "3":
            nama = input("Masukkan nama perlengkapan: ")
            toko.cari_perlengkapan(nama)
        elif pilihan == "4":
            nama = input("Nama perlengkapan yang ingin diupdate: ")
            jenis = input("Jenis: ")
            harga = int(input("Harga: "))
            jumlah = int(input("Jumlah: "))
            toko.update_perlengkapan(nama, jenis, harga, jumlah)
        elif pilihan == "5":
            nama = input("Nama perlengkapan yang ingin dihapus: ")
            toko.hapus_perlengkapan(nama)
        elif pilihan == "6":
            print("Terima kasih telah menggunakan layanan Pink Velvet Athletics!!!!!")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih menu yang sesuai.")

if __name__ == "__main__":
    main()
