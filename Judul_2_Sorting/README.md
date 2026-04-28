Sistem Pengurutan Stok Barang

Progam ini berfungsdi sebagai mengelola stok barang yang ada di toko secara efisien. yang dimana user nya dapat memasukkan jumlah jenis barang beserta stok nya masing masing, yang kemudian progam ini akan mengurutkan data stok barang dari yang terkecil ke yang terbesar dengan mengunakan algoritma bubble sort. setelah mengurutkan, progam akan menampilkan stok sebelum dan sesudah pengurutan dan juga menampilkan jumlah stok yang ada. progam ini akan cukup berguna untuk pemilik toko karena memperioritaskan pengisian ulang stok barang yang paling sedikit, sehingga dapat menjaga kestabilan stok yang ada di toko

<img width="760" height="1009" alt="Screenshot 2026-04-28 213850" src="https://github.com/user-attachments/assets/d20aa9ff-94e0-4d27-9777-6e378a241131" />

def tukar(arr, i, j) # membuat fungsi tukar i, j

temp = arr[i]  # menyimpan nilai (i) kedalam penyimpanan sementara

arr[i] = arr[j]  # Isi arr[i] dengan nilai arr[j]

arr[j] = temp   # mengisi array j dengan nilai yang disimpan sebelumnya

def bubble_sort(arr, n): # membuat fungsi sorting

for i in range(n - 1):  # mwnjalankan jumlah literasi sebanyak n-1

for j in range(n - i - 1): # membandingkan elemen yang bersebelahan 

if arr[j] > arr[j + 1]:  # melihat apakah nilai nya lebih besar dari nilai selanjutnya

tukar(arr, j, j + 1) # berfungsi untuk menukar nilai jika nilainya lebih besar

n = int(input("Masukkan jumlah jenis barang: ")) # untuk menginput jumlah barang 

except ValueError: # untuk menghentikan jika salah menginput nilai

print("Input tidak valid!") # menampilkan tulisan seperti itu jika salah menginput

return # untuk menghentikan fungsi

arr = []  # sebagai array kosong

for i in range(n): # perulangan sebanyak n kali

 while True:   # loop sampai inpudnya valid

 stok = int(input(f"Stok barang ke-{i+1}: ") # untuk menginput stok 

  if stok >= 0:  # cek stok valid

   arr.append(stok)   # menambahkan stok ke dalam array 

     break   # keluar dalam kondisi perulangan 

   else:
                print("Stok tidak boleh negatif!")
        except ValueError:
            print("Input tidak valid, masukkan angka >= 0!") # kalau inputan nya negatif maka dia akan menampilkan kata "inputan tidak valid" lalu dia akan mengulang di bagian user menginput stok

print(f"\nStok barang sebelum diurutkan: {arr}")   # menampilkan array yang belum di urutkan

bubble_sort(arr, n)   # untuk memanggil fungsi sorting

print("Stok barang setelah diurutkan (Bubble Sort):", end=" ") # menampilkan data yang sudah diurutkan 

print(f"Total stok: {sum(arr)} buah")     # untuk menghitung jumlah stok dan menampilkan totalnya

<img width="621" height="222" alt="Screenshot 2026-04-28 220721" src="https://github.com/user-attachments/assets/557e0819-1845-450a-9eb4-41009b0a7d89" />

di awal kita diminta menginputkan jumlah jenis barang, dan setelahnya kita diminta memasukan jumlah stok barang yang ingin ditambahkan. lalu yang pertama dia akan menampilkan stok barang yang belum di urutkan lalu yang kedua progam menampilkan stok barang yang sudah diurutkan. dan yang terakhir progam akan menjumlahkan total dari stok yanmg ada.

link youtube : https://youtu.be/xJ4AKDQcV_I?si=pVFVkeqR04DE9rfv
