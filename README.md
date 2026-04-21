Sistem Menejemen Inventory Toko 

Progam ini adalah aplikasi untuk mengelola stok barang toko/gudang. pengguna dapat menambah produk baru (nama, harga, stok awal) dengan kode yang menyimpan data tersebut seperti (p01, p02), dapat melihat dafatr stok apakah masih banyak atau sedang menipis kalau menipis ditandai dengan tanda ⚠, disini juga dapat mencari produk berdasarkan nama atau code yang sudah tersimpan sebelumnya, disini juga dapat mengupdate stok dan monitoring stok yang mau habis secara real time. progam ini dirancang untuk umkm yang butuh sistem sederhana tanpa database eksternal

Dalam progam ini menggunakan python list sebagai struktur data utama dengan algoritma linear search 0(n) untuk semua operasi yang efesien untuk menangani <1000 item.

<img width="1031" height="661" alt="Screenshot 2026-04-21 212535" src="https://github.com/user-attachments/assets/aa3adb75-ed10-4f9b-a9ff-85b1e4a0c8c1" />

<img width="960" height="592" alt="Screenshot 2026-04-21 212603" src="https://github.com/user-attachments/assets/bfc0a600-7bfd-49d8-a420-4e11499bced4" />

import datetime # Import modul datetime

produk = []  # List kosong sebagai "database" untuk penyimpanan produk

def tambah():
    n = len(produk) + 1 # untuk menghitung jumlah produk + 1 dan angka 1 untuk buat kode unik

    p = {
        "kode": f"P{n:02d}", # Kode otomatis yang akan terbuat: P01, P02, dst (2 digit)

        "nama": input("Nama: ") # user bisa menginputkan sendiri nama produk

        "harga": float(input("Harga: ")),# untuk menginput harga lalu dikonversi ke float

         "stok": int(input("Stok: ")), # untuk menginput jumlah stok lalu dikonversi ke integer

         "sat": "pcs" # memberi nama satuan barangnya dengan code = "pcs"

produk.append(p) # untuk menambahkan barang yang sudah diinput ke list

print(f"✓ {p['nama']} ({p['kode']})") # Konfirmasi penambahan barang

if not produk: return print("Kosong") # Jika list kosong maka akan menampilkan "Kosong" lalu keluar

for p in produk: # untuk Loop setiap produk

flag = " ⚠" if p["stok"] <= 3 else ""  # Tandai ⚠ terjadi jika stok ≤ 3 (menipis)

def cari(kw):
    for p in produk:
        # Cari berdasarkan nama (case-insensitive) ATAU kode (huruf besar)
        if kw.lower() in p['nama'].lower() or p['kode'] == kw.upper():
            print(f"{p['kode']} {p['nama']} Rp{p['harga']:,} stok:{p['stok']}") # digunakan mencari baranmg yang sudah tersimpan dalam data, dengan menginput kode unik saat barang di tambahkan ke dalam progam

def stok(kode, jml, op): # fungsi untuk memberikan update stok

  if p['kode'] == kode # untuk menemukan produk berdasarkan kode

    p['stok'] += jml #untuk menambah stok

 if jml > p['stok']: # Validasi stok tidak boleh minus

  p['stok'] -= jml # untuk mengurangi stok

   print(f"{p['nama']}: stok={p['stok']}")
            return               # Keluar setelah berhasil update

            print("Kode salah!") # Jika kode tidak ditemukan

while True: # untuk menampilkan menu dan jumlah item saat ini

if c == '1': tambah() # Panggil fungsi tambah

 elif c == '2': tampil()  # Panggil fungsi tampil

 elif c == '3': cari(input("Cari: ")) # Input keyword lalu cari

 kode = input("Kode: ").upper() # Input kodenya akan diubah huruf besar

 op = input("+/-(tambah/kurang): ") # Pilih operasi + atau -

 stok(kode, int(input("Jml: ")), op)# Input jumlah lalu update stok

 elif c == '0': break # Keluar dari loop maka program selesai

 OUTPUT:

 <img width="592" height="53" alt="Screenshot 2026-04-21 220937" src="https://github.com/user-attachments/assets/595b3cad-d218-4bec-9dbd-ac0015e86b83" />

saat progam dijalankan maka tampilan awal kita disuruh memilih menu apa yang akan dijalankan

<img width="603" height="146" alt="Screenshot 2026-04-21 221304" src="https://github.com/user-attachments/assets/490b8682-5b77-490a-9f00-19dd9c4fbf6f" />

kalau kita memilih 1 maka kita disuruh mengisi data seperti nama barang,harga,dan stok. setelah tersimpan maka akan diberikan code unik untuk kita bisa mengakses barang tersebut dengan menginputkan code uniknya

<img width="608" height="154" alt="Screenshot 2026-04-21 221637" src="https://github.com/user-attachments/assets/be2661d6-0fa8-4bf5-8519-6cba92014d99" />

kalau kita memilih 2 maka dia akan menampilkan semua inputan atau barang yang kita simpan sebelumnya lengkap dengan nama barangnya serta stoknya

<img width="593" height="118" alt="Screenshot 2026-04-21 221840" src="https://github.com/user-attachments/assets/53b1f398-d9df-4eef-bd64-bffbff2d8b3d" />

saat kita memilih 3 ini berfungsi untuk mencari produk yang sudah disimpan dengan mamasukan coide unik untuk mengakses data barang yang ingin kita lihat

<img width="599" height="150" alt="Screenshot 2026-04-21 222203" src="https://github.com/user-attachments/assets/d244194d-014d-4322-b71e-186f3ee93097" />

di pilihan 4 itu berfungsi sebgai penambah atau mengurangi stok barang

<img width="672" height="80" alt="Screenshot 2026-04-21 222431" src="https://github.com/user-attachments/assets/ec34ac90-9731-4b46-87df-525642e88e58" />

di pihan 5 berfungsi apakah ada barang yang stok nya sedang menipis, kalau stok barang sedang menipis maka dia akan menampilkan barang yang stok nya menipis itu

<img width="959" height="83" alt="Screenshot 2026-04-21 222752" src="https://github.com/user-attachments/assets/8e247ded-d903-4fe9-a3bc-5e73536b2bdb" />

untuk 6 adalah untuk mengakhiri progam

youtube:
https://youtu.be/J8JfVngAq2g?si=I3XQbt5nlsv9n99v
