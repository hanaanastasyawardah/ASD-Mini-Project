import os
from prettytable import PrettyTable

# Deklarasi class node 
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

# Deklarasi class linkedlist
class LinkedList:
    def __init__(self):
        self.head = None

    # Menambahkan data di awal linked list
    def tambah_di_awal(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    # Menambahkan data di akhir linked list
    def tambah_di_akhir(self, data):
        if not self.head:
            self.head = Node(data)
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = Node(data)
    
    # Menambahkan data di tengah linked list
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

    # Menghapus data di awal linked list
    def hapus_di_awal(self):
        if not self.head:
            print("Linked list sudah kosong.")
            return
        self.head = self.head.next
    
    # Menghapus data di akhir linked list
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
    
    # Menghapus data di tengah linked list
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
    
    # Mencetak data linked list
    def cetak_linked_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

# Deklarasi kelas Toko Olahraga
class TokoOlahraga:
    def __init__(self):
        self.perlengkapan = LinkedList()
    
    # Menambahkan data perlengkapan
    def tambah_perlengkapan(self, data):
        self.perlengkapan.tambah_di_akhir(data)
        print("Perlengkapan berhasil ditambahkan.")
    
    # Menambahkan data perlengkapan di awal
    def tambah_perlengkapan_awal(self, data):
        self.perlengkapan.tambah_di_awal(data)
        print("Perlengkapan berhasil ditambahkan di awal.")
    
    # Menambahkan data perlengkapan di tengah
    def tambah_perlengkapan_tengah(self, posisi, data):
        self.perlengkapan.tambah_di_antara(posisi, data)
        print("Perlengkapan berhasil ditambahkan di tengah.")
    
    # Menambahkan data perlengkapan di akhir
    def tambah_perlengkapan_akhir(self, data):
        self.perlengkapan.tambah_di_akhir(data)
        print("Perlengkapan berhasil ditambahkan di akhir.")
    
    # Menampilkan data perlengkapan
    def lihat_perlengkapan(self):
        table = PrettyTable(["ID", "Nama", "Jenis", "Harga", "Jumlah"])
        if not self.perlengkapan.head:
            print("Daftar Perlengkapan Olahraga masih kosong.")
            return
        current = self.perlengkapan.head
        while current:
            table.add_row([current.data['ID'], current.data['Nama'], current.data['Jenis'], current.data['Harga'], current.data['Jumlah']])
            current = current.next
        print("Daftar Perlengkapan Olahraga:")
        print(table)
    
    # Mencari data perlengkapan
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
    
    # Mengupdate data perlengkapan
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
    
    # Menghapus data perlengkapan
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
        
    # Sorting data perlengkapan berdasarkan ID
    def sort_by_id(self, ascending=True):
        if not self.perlengkapan.head:
            print("Daftar Perlengkapan Olahraga masih kosong.")
            return
        self.perlengkapan.head = self.quick_sort(self.perlengkapan.head, ascending, key='ID')
        print("Perlengkapan berhasil disorting berdasarkan ID.")

    # Sorting data perlengkapan berdasarkan nama
    def sort_by_nama(self, ascending=True):
        if not self.perlengkapan.head:
            print("Daftar Perlengkapan Olahraga masih kosong.")
            return
        self.perlengkapan.head = self.quick_sort(self.perlengkapan.head, ascending, key='Nama')
        print("Perlengkapan berhasil disorting berdasarkan Nama.")
        self.lihat_perlengkapan()
        
    # Algoritma quick sort
    def quick_sort(self, start, ascending=True, key='ID'):
        if start is None or start is None:
            return start

        pivot_prev = start
        pivot = start

        cur = pivot.next
        pivot.next = None
        if key == 'ID':
            id_val = pivot.data['ID']
        else:
            id_val = pivot.data['Nama']
        pivot.next = None

        lesser_head = Node(None)
        lesser = lesser_head
        greater_head = Node(None)
        greater = greater_head

        while cur:
            if key == 'ID':
                if ascending and cur.data['ID'] < id_val or not ascending and cur.data['ID'] > id_val:
                    lesser.next = cur
                    lesser = lesser.next
                else:
                    greater.next = cur
                    greater = greater.next
            else:
                if ascending and cur.data['Nama'] < id_val or not ascending and cur.data['Nama'] > id_val:
                    lesser.next = cur
                    lesser = lesser.next
                else:
                    greater.next = cur
                    greater = greater.next
            cur = cur.next

        lesser.next = None
        greater.next = None

        lesser_sorted = self.quick_sort(lesser_head.next, ascending, key)
        greater_sorted = self.quick_sort(greater_head.next, ascending, key)

        if lesser_sorted is None:
            pivot.next = greater_sorted
            return pivot

        lesser_tail = lesser_sorted
        while lesser_tail.next:
            lesser_tail = lesser_tail.next

        lesser_tail.next = pivot
        pivot.next = greater_sorted

        return lesser_sorted

# Sorting Data
    def sort(self, by_name=True, ascending=True):
        if by_name:
            self.sort_by_nama(ascending)
        else:
            self.sort_by_id(ascending)

# Setelah pengurutan selesai, tampilkan daftar perlengkapan
            self.lihat_perlengkapan()
        
# Fungsi main
def main():
    toko = TokoOlahraga()

    daftar_peralatan = [{
        "Nama": "Sepatu Lari", "Jenis": "Sepatu", "Harga": 250000, "Jumlah": 10, "ID": 1
    },
        {
            "Nama": "Bola Basket", "Jenis": "Bola", "Harga": 150000, "Jumlah": 20, "ID": 2
        },
        {
            "Nama": "Raket Tennis", "Jenis": "Raket", "Harga": 200000, "Jumlah": 15, "ID": 3
        },
        {
            "Nama": "Baju Renang", "Jenis": "Pakaian", "Harga": 100000, "Jumlah": 25, "ID": 4
        },
        {
            "Nama": "Sarung Tinju", "Jenis": "Alat Tinju", "Harga": 300000, "Jumlah": 5, "ID": 5
        },
        {
            "Nama": "Trampolin", "Jenis": "Alat Pelatihan", "Harga": 100000, "Jumlah": 15, "ID": 6
        },
        {
            "Nama": "Papan Selancar", "Jenis": "Perlengkapan Selancar", "Harga": 500000, "Jumlah": 3, "ID": 7
        },
        {
            "Nama": "Treadmill", "Jenis": "Alat Olahraga Elektronik", "Harga": 2000000, "Jumlah": 2, "ID": 8
        },
        {
            "Nama": "Raket Bulutangkis", "Jenis": "Raket", "Harga": 150000, "Jumlah": 12, "ID": 9
        },
        {
            "Nama": "Jersey Basket", "Jenis": "Pakaian", "Harga": 120000, "Jumlah": 15, "ID": 10
        }]

    for peralatan in daftar_peralatan:
        toko.tambah_perlengkapan(peralatan)

    while True:
        os.system("cls")
        os.system("clear")
        print("\n🌺=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=🌺")
        print("+                       SELAMAT DATANG                           +")
        print("+                PINK VELVET ATHLETICS ૮₍´˶• . • ⑅ ₎ა            +")
        print("+                    SILAHKAN PILIH MENU                         +")
        print("🌺=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+")
        print("1. TAMBAH PERLENGKAPAN                                           +")
        print("2. LIHAT PERLENGKAPAN                                            +")
        print("3. CARI PERLENGKAPAN                                             +")
        print("4. UPDATE PERLENGKAPAN                                           +")
        print("5. HAPUS PERLENGKAPAN                                            +")
        print("6. SORTING                                                       +")
        print("7. EXIT                                                          +")
        print("🌺=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=🌺")

        pilihan = input("Masukkan pilihan Anda: ")

        if pilihan == "1":
            print("\n🎀=+=+=+=+=+=+=PILIH METODE SORTING=+=+=+=+=+=+=+=+=+=🎀")
            print("+                                                     +")
            print("[1.] TAMBAH PERLENGKAPAN DI AWAL                      +")
            print("[2.] TAMBAH PERLENGKAPAN DI TENGAH                    +")
            print("[3.] TAMBAH PERLENGKAPAN DI AKHIR                     +")
            print("+                                                     +")
            print("🎀=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+==+=+=+=+=+=+=+=🎀")
            pilihan_tambah = input("Pilih jenis penambahan perlengkapan: ")
            if pilihan_tambah == "1":
                data = {
                    "Nama": input("Nama: "),
                    "Jenis": input("Jenis: "),
                    "Harga": int(input("Harga: ")),
                    "Jumlah": int(input("Jumlah: ")),
                    "ID": int(input("ID: "))
                }
                toko.tambah_perlengkapan_awal(data)
            elif pilihan_tambah == "2":
                posisi = int(input("Posisi: "))
                data = {
                    "Nama": input("Nama: "),
                    "Jenis": input("Jenis: "),
                    "Harga": int(input("Harga: ")),
                    "Jumlah": int(input("Jumlah: ")),
                    "ID": int(input("ID: "))
                }
                toko.tambah_perlengkapan_tengah(posisi, data)
            elif pilihan_tambah == "3":
                data = {
                    "Nama": input("Nama: "),
                    "Jenis": input("Jenis: "),
                    "Harga": int(input("Harga: ")),
                    "Jumlah": int(input("Jumlah: ")),
                    "ID": int(input("ID: "))
                }
                toko.tambah_perlengkapan_akhir(data)
            else:
                print("Pilihan tidak valid.")
        elif pilihan == "2":
            toko.lihat_perlengkapan()
            input("Tekan Enter untuk kembali ke menu...")
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
            print("\n🎀=+=+=+=+=+=+=PILIH METODE SORTING=+=+=+=+=+=+=+=+=+=🎀")
            print("                                                      +")
            print("[1.] SORT BY ID (Ascending)                           +")                     
            print("[2.] SORT BY ID (Descending)                          +")
            print("[3.] SORT BY NAMA (Ascending)                         +")
            print("[4.] SORT BY NAMA (Descending)                        +")
            print("                                                      +")
            print("🎀=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=")
            pilihan_sort = input("Pilih metode sorting: ")
            if pilihan_sort == "1":
                toko.sort(by_name=False, ascending=True)
            elif pilihan_sort == "2":
                toko.sort(by_name=False, ascending=False)
            elif pilihan_sort == "3":
                toko.sort(by_name=True, ascending=True)
            elif pilihan_sort == "4":
                toko.sort(by_name=True, ascending=False)
            else:
                print("Pilihan tidak valid.")
            input("Tekan Enter untuk kembali ke menu...")
        elif pilihan == "7":
            print("\n🎀=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=🎀")
            print("+                ⋆꙳•̩̩͙❅*̩̩͙‧͙ ‧͙*̩̩͙❆ ͙͛ ˚₊⋆                  ⋆꙳•̩̩͙❅*̩̩͙‧͙ ‧͙*̩̩͙❆ ͙͛ ˚₊⋆          +")
            print("+                                 TERIMA KASIH                             +")
            print("+               TELAH MENGGUNAKAN LAYANAN PINK VELVET ATHLETICS!           +")   
            print("+                                                                          +")                                           
            print("🎀=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=🎀")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih opsi yang benar.")

if __name__ == "__main__":
    main()

