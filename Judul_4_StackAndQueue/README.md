SIMULASI KERANJANG MENGUNAKAN ALGORITMA STACK

progam ini adalah simulasi keranjang belanja yang ada di toko yang memungkinkan pelanggan bisa menambahkan barang, menghapus barang terakhir yang dimasukkan, melihat barang barang yang dimasukkan , serta melihat barang apa saja yang dimasukkan ke dalam keranjang. pelanggan cukup memilih menu yang tersedia dalam progam dan memasukkan barang yang diinginkan.

progam ini menggunakan struktur data stack yang menggunakan array sebagai wadah penyimpanannya. stack ini bekerja dengan prinsip LIFO yang dimana data terakhir yang dimasukkan adalah data yang pertama kali dikeluarkan.

<img width="807" height="953" alt="Screenshot 2026-05-13 214114" src="https://github.com/user-attachments/assets/7e462ac0-d4e7-41ca-8273-10fac3f859e3" />

<img width="512" height="872" alt="Screenshot 2026-05-13 214128" src="https://github.com/user-attachments/assets/aeb5a77b-10ff-49b9-bde2-7a9cb344bbee" />

class StackArray: # ini digunakan untuk mendefinisikan sebuah class bernama stackarray

def __init__(self, max_size=100): # membuat definisi inisiasi yang akan otomatis dipanggil saat objek dibuat dengan parameter max_size=100 yang artinya batas maksimal penyimpanan array nya adlah 100

self.MAX = max_size # menyimpan ukuran maksimum stack ke atribut max 

self.st = [None] * self.MAX # membuat array kosong sebanyak batas maksimal yang dibuat

self.top_idx = -1 # ini adalah untuk index paling atas di dalam stack yang dimana -1 berarti stack nya masih kosong 

def is_empty(self):
    return self.top_idx == -1 # mengecek apakah stack sedang kosong, dia akan tru bila top nya -1 dan false bila jika sudah terisi

def is_full(self):
    return self.top_idx == self.MAX - 1 # mengecek apakah stack dalam keadaan penuh atau tidak 

def push(self, x): # membuat fungsi menambahkan elemen ke atas stack

if self.is_full():
        print("Stack penuh")
        return # jika stack penuh maka akan mencetak stack penuh dan return berfungsi untuk memberhentikan perintah.

self.top_idx += 1 # menaikkan top nya satu langkah ke atas untuk menyiapkan slot baru

 self.st[self.top_idx] = x # menyimpan nilai x ke posisi top yang baru ke dalam array.

print(f"Push {x} berhasil") # akan mencetak berhasil bila operasi push berhasil dilakukan 

def pop(self): # membuat fungsi pop atau fungsi untuk menghapus elemen yang paling atas 

 if self.is_empty():
        print("Stack kosong")
        return # jika stack kosong akan mencetak stack kosong.

print(f"Pop {self.st[self.top_idx]} berhasil") # mencetak data yang berhasil di hapus 

self.top_idx -= 1 menurunkan top satu langkah

def display(self):
    if self.is_empty():
        print("Stack kosong")
        return # mengecek apakah stack kosong, jika kosong maka akan mencetak pesan dan berhenti

 for i in range(self.top_idx, -1, -1): # ini akan menampilkan elemen paling atas ke yang paling bawah

print(self.st[i], end=" ") # mencetak setiap elemen  yang dipsah spasi tanpa pindah baris

def main():
    keranjang = StackArray() # membuat fungsi utama yang disimpan dalam variabel keranjang

 while pilih != 5: # loop akan berjalan terus selagi bukan memilih 5

pilih = int(input("Pilih: ")) # meminta inputan dari user yang berupa string 

except ValueError:
            print("Input tidak valid!")
            continue # jika user memasukkan simbol simbol yang bukan huruf atau angka maka akan menangkap eror dari inputannya dan akan mengulang ke awal

if pilih == 1:
            val = input("nama barang: ")
            keranjang.push(val) # jika memilih 1 maka akan memanggil fungsi push

elif pilih == 2:
            keranjang.pop() # jika memilih 2 maka akan memanggil fungsi pop

 elif pilih == 3:
            keranjang.peek() # jika memilih 3 maka akan melihat elemen paling atas

 elif pilih == 4:
            keranjang.display() # jika memilih 4 maka akan menampilkan seluruh stack

elif pilih == 5:
            print("Terima kasih!")# jika memilih 5 maka akan mengakhiri progam dan mencetak pesan terimakasih.



link YOUTUBE : https://youtu.be/QiKl8MoWs88?si=LF6iPf8Xep9wbdrd
