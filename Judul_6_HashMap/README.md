SISTEM PARKIR KENDARAAN 

Progam ini merupakan sistem parkir sederhana yang berfungsi untuk mencatat kendaraan yang masuk dan yang keluar area parkir dengan mengunakan nomor tiket sebagai pengindentifikas. Jadi ketika kendaraan masuk, nomor tiket dan nomor plat kendaraan di disimpan ke dalam hash table. saat kendaraan keluar sistem akan mencari data berdasarkan nomor tiket dan menampilkan informasi kendaraan lalu menghapus data tersebut dari hash table, hal ini dapat memudahkan dalam mengelola parkir dalam memantau kendaraan yang terparkirkan secara real time.

Algoritma yang digunakan adalah hash table dengan separate chaining. jadi setiap data memiliki kunci yang di ubah menjadi index melalui fungsi hash.

<img width="708" height="1050" alt="Screenshot 2026-06-07 215558" src="https://github.com/user-attachments/assets/43fb0d25-7354-49e4-a6f4-35d101641e2a" />

<img width="718" height="1001" alt="Screenshot 2026-06-07 215614" src="https://github.com/user-attachments/assets/35e0178e-2335-4fa7-be97-8dfe6e52c1a7" />

<img width="646" height="568" alt="Screenshot 2026-06-07 215623" src="https://github.com/user-attachments/assets/e12d42f9-e50c-445c-9ee0-d6e6b9b16584" />

class Node: # mendefinisikan calss node yang akan digunakan 

def __init__(self, key, value): # membuat definisi dari inisisi yang memiliki parameter key dan value

self.key = key # berfungsi untuk menyimpan kunci nya

self.value = value # berfungsi untuk menyimpan nilai nya

self.next = None # digunakan untuk menghubungkan ke node berikutnya

class HashMapSeparateChaining: # mendefinisikan class dari hash map yang mengunakan metode separate chaining 

self.SIZE = size # menyimpan ukuran hash table nya ke dalam atribut size 

 self.table = [None] * self.SIZE # membuat list dengan jumlah size yang sudah ditentukan sebelunmnya dan semuanya masih kosong

def hash_function(self, key): # fungsi untuk menghitung index hash dari sebuah key

return (key % self.SIZE + self.SIZE) % self.SIZE # digunakan untuk menghitung key untuk mendapatkan index

def insert(self, key, value): # membuat fungsi insert dengan parameter key dan value

index = self.hash_function(key) # menghitung index mengunakan fungsi hash

current = self.table[index] # menyimpan head dari linked list ke variabel current

while current is not None: # dia akan me looping selama belum mencapai akhir

if current.key == key: # ngecek apakah key sudah ada dalam linked list 

current.value = value # kalau kuy nya sudah ditemukan maka akan memperbarui nilai yang baru 

current = current.next # pindah ke node berikutnya

new_node = Node(key, value) # jika key tidak ditemukan maka akan memnbuat node baru

new_node.next = self.table[index] # menghubungkan node baru ke head link list 

self.table[index] = new_node # menjadikan node baru menjadi head baru

def search(self, key): # membuat fungsi pencarian

index = self.hash_function(key) # menghitung index key nya seharusnya berada di mana 

current = self.table[index] # akan memulai dari head linked list nya

if current.key == key: # jika key nya sudah ditemukan 

current = current.next # pindah ke node selanjutnya

def remove_key(self, key): membuat fungsi untuk menghapus node berdasarkan kuncinya

index = self.hash_function(key) # digunkan untuk menghitung index nya

current = self.table[index] # memulai nya dari head linked list

prev = None # variabel untuk menyimpan referensi node sebelumnya

if current.key == key: # kondisi jika key nya sudah ditemukan 

if prev is None: # ngecek apakah node yang dihapus adalah head

self.table[index] = current.next # jika ya maka akan memperbarui head menjadi node berikutnya 

prev = current # akan meng update prev ke node saat ini sebelum berpindah

current = current.next # pindah ke node berikutnya

def display(self): # membuat fungsi untuk menampilkan seluruh isi dari hash table

for i in range(self.SIZE): # akan looping dari 0

print(f"{i}: ", end="") # mencetak nomor index

 current = self.table[i] # Mulai dari head linked list ke-i

 print(f"({current.key},{current.value}) -> ", end="") # Cetak key dan value setiap node

current = current.next # pindah ke node berikutnya

def main(): # fungsi utama program

print("    SISTEM PARKIR") # cetak judul program

print("\n1. Masuk")
print("2. Keluar")
print("3. Lihat")
print("0. Selesai") # tampilan menu pilihan

 pilih = input("Pilih: ")

        if pilih == "0":
            break # jika pilih 0 maka progam akan berhenti

elif pilih == "1": jika pilih satu

tiket = int(input("No Tiket: ")) # meminta user untuk mengiputkan no tiket nya

plat = input("Plat Nomor: ") # menginputkan palt kendaraan

parkir.insert(tiket, plat) # untuk menyimpan data ke hash table

print(f"Tiket {tiket} - {plat} masuk") # cetak konfirmasi berhasil

elif pilih == "2": # jika pilih 2 

tiket = int(input("No Tiket: ")) menginput no tiket 

hasil = parkir.search(tiket) # mencari data tiket di hash table

print(f"{hasil.value} keluar, bayar Rp5000") # menampilkan plat nomor dan biaya parkir

parkir.remove_key(tiket) # menghapus data tiket dari hash table

elif pilih == "3": # jika milih 3

parkir.display() # Panggil method display untuk tampilkan isi hash table

<img width="431" height="587" alt="Screenshot 2026-06-07 225504" src="https://github.com/user-attachments/assets/a02e3ed4-711a-410a-9a3a-c533648aed6f" />

<img width="317" height="294" alt="Screenshot 2026-06-07 225512" src="https://github.com/user-attachments/assets/6f3f4fe9-f6f6-4016-80d1-e898bff1bce8" />

jadi saat menjalankan progamnya maka yang akan di tampilkan pertama kali adalah judul sistemnya dan menu pilihannya, kalau memilih no 1 maka user diminta menginputkan no tiket dan no plat dari kendaraan nya lalu menampilkan notifikasi bahwa kendaraan tersebut sudah masuk. kalau memilih 2 maka user diminta untuk memasukkan no tiket nya dan sistem akan menghapus kendaraan tersebut dari list dan menampilkan notifikasi bahwa kendaraan nya sudah keluar dan juga menampilkan harga yang harus dibayarkan pengguna kendaraan saat parkir. kalau pilih no 3 maka akan menampilkan seluruh isi dari hash table nya. kalau memilih 3 maka akan memberhentikan sistemnya.


LINK YOUTUBE : https://youtu.be/xOKe_LhmC58?si=dwt48q3JmZcyMa7K
