PENCARIAN BARANG PADA KATALOG TOKO

jadi progam ini digunakan untuk mencari produk pada katalog di toko, yang dimana dapa isi katalog ada 10 jenis produk kebutuhan sehari hari yang sudah terurut. yang pertama si user akan dimintai memasukkan nama produk yang pengen dicari lalu progam akan memeriksa apakah barang yang dicari user ada pada katalog di toko tersebut.

algoritma yang dipakai pada progam ini adalah binary search, pada algoritma ini berkerja pada data yang sudah terurut, yang dimana cara kerja dari algoritma ini adalah dengan cara membagi dua array lalu prgam akan mengecek pada tengah elemen lalu membandingkannya apakah akan dijalankan disebelah kiri atau di sebelah kanan.

<img width="601" height="647" alt="Screenshot 2026-05-05 224458" src="https://github.com/user-attachments/assets/0cc14102-6d60-49ab-ac4b-8aaeeba43597" />

<img width="808" height="552" alt="Screenshot 2026-05-05 224513" src="https://github.com/user-attachments/assets/6639a9f4-2882-4088-b72e-91ba00de3e0c" />

katalog = [
    "Beras",
    "Deterjen",
    "Gula",
    "Kecap",
    "Mie",
    "Minyak",
    "Sabun",
    "Sampo",
    "Susu",
    "Teh",
] # mendefinisikan list katalog yang berisi 10 nama produk yang suda terurut 

def binary_search(arr, n, target): # mendefinisikan dungsi binary search dengan tiga parameter arr : list yang akan dicari, n: panjangnya, target: barang yang ingin dicari

 l = 0 , r = n - 1 # yang pertama sebagai index paling kiri yang dimulai dari 0, kalau yang kedua adalah index yang paling kanan n - 1

 pos = - 1 # posisi ditemukan nya target (-1) berarti belum ditemukan 

 while l <= r: # kalau 1 masih lebih kecil datauy sama dengan r, maka pencarian masih valid

   m = l + (r - l) // 2 # menghitung index tengah

   print(f"Median: {m}, produk: {arr[m]}") # menampilkan nilai tengah dari produk 

     if arr[m].lower() == target.lower(): # membandingkan produk di index dengan target, dengan mengubahnya huruf menjadi kecil biar tidak sensitif

    pos = m
    break # kalau datanya cocok maka dia akan menyimpan index m ke pos, lalu keluar dari loop 

        elif arr[m].lower() < target.lower():
            print("Mencari di kanan")
            l = m + 1 # jika produk lebih kecil dari dari target, makatarget nya berada di sisi kanan. dengan menggeser l ke m + 1 sehingga pencarian berikutnya hanya pada bagian kanan.

            else:
            print("Mencari di kiri")
            r = m - 1 # kalau target lebih besar dari terget maka yang ditargetkan berada pada sisi kiri. lalu menggeser r ke m - 1 lalu pencarian berikutnya akan berlanjut ke bagian kiri

            return pos # mengembalikan nilai pos jika data nya ditemukan

  def main(): # membuat fungsi utamanya

   n = len(katalog) # untuk menghitung panjang dari katalog

   print("Daftar produk (terurut A-Z):") # menampilkan tulisan seperti diamping saat panjang katalognya berhasil dijalankan

   for i in range(n):
        print(f"  [{i}] {katalog[i]}") # mencetak semua produk yang ada dalam katalog bersama dengan indexnya

   target = input("\nMasukkan nama produk yang ingin dicari: ") # berfungsi sebagai user nya dapat menginputkan nama barang yang ingin dicari

   pos = binary_search(katalog, n, target) # digunakan untuk memanggil fungsi dari binary

   if pos != -1: # akan negecek apakah pos bukan -1 

  print(f"Produk ditemukan pada indeks ke-{pos}: {katalog[pos]}") # kalau bukan -1 maaka akan mencetak index dan nama indexnya

   else:
        print("Produk tidak ditemukan") # kalau  tidak ditemukan maka dia sksn mencetak produk tidak ditemukan

   <img width="624" height="426" alt="Screenshot 2026-05-05 234007" src="https://github.com/user-attachments/assets/51fac638-ac5f-4910-afbe-77a882d8933a" />

  ditampilan pertama akan langsung menampilkan nama nama produk yang ada di katlog beserta letak indexnya, lalu yang kedua user diminta memasukkan nama barang yang ingin dicari, setelah itu progam akan menentukan nilai tengah lalu membandingkan apakah dia lebih kecil apa lebih besar karena lebih kecil maka operasi akan dilanjutkan disebelah kiri, lalu mengecek lagi apakah itu lebih besar apa lebih kecil karena lebih kecil maka akan di cek lagi di bagian kiri, lalu pada index 0 ternyata data cocok dengan apa yang dicari. maka dia akan mencetak bahwa produk telah ditemukan dan memberikan informasi barang tersebut pada posisi index ke berapa.

link youtube : https://youtu.be/FPLFuSc_OO0?si=d-DDcrJWu67EgMcI
