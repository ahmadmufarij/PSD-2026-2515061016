Sistem Manajemen Stok Toko Sembako Menggunakan Binary Search Tree

progam ini merupakan sistem menejemen stok yang dirancang membantu pengelolaan produk pada toko sembako. fungsi utama dari progam ini itu mencakup penambahan produk baru beserta informasi nama,jumlah stok, dan harga, dan dapat dilakukan pencarian produk berdasarkan dari jumlah stok yang ada serta menampilkan seluruh produk dalam berbagai urutan. di progam ini juga menyediakan fitur yang dimana dapat menemukan produk yang jumlah stok nya paling sedikit atau yang paling banyak dan dapat menghitung total dari stok barang yang ada. dengan adanya fitur fitur ini semoga bisa memudahkan pemilik toko dalam memantau dan mengelola ketersedian barang secara efisien.

algoritma yang digunakan dalam progam ini adalah binary search tree yang dimana algoritma ini yang dimana di setiap node memiliki paling banyak dua anak, dengan aturan anak kiri harus lebih kecil dan nilai anak dari kanan harus selalu lebih besar dari node induknya.

<img width="983" height="997" alt="Screenshot 2026-05-18 230433" src="https://github.com/user-attachments/assets/03e5e53c-9c29-400c-9103-8fb11d6783cf" />

<img width="1033" height="987" alt="Screenshot 2026-05-18 230450" src="https://github.com/user-attachments/assets/a8cb405a-69fd-4b84-ad30-389a0fea9bc5" />

<img width="861" height="946" alt="Screenshot 2026-05-18 230507" src="https://github.com/user-attachments/assets/f37b25f0-eafb-4732-82e3-d821317c91c4" />

class Node: # mendefinisikan sebuah class node 

 def __init__(self, nama, stok, harga): # mendefinisikan insiasi dengan parameter nama, stok, harga

  self.key = stok # menetapkan stok sebagai kunci dari node ini dan kunci ini akan dipakai oleh bst untuk menentukan posisi dari node nya

self.nama = nama # berfungsi sebagai penyimpanan nama produk

self.harga = harga # Menyimpan harga produk dalam rupiah sebagai atribut node

self.left = self.right = None # membuat pointer kanan dan kiri dalam kondisi kosong 

class BST: # Mendefinisikan class Binary Search Tree

self.root = None # Menetapkan root sebagai None, artinya pohon masih kosong, belum ada produk sama sekali.

def insert(self, nama, stok, harga): #  untuk menyisipkan produk baru ke dalam pohon BST. Menerima nama, stok, dan harga produk.

def _ins(root): # Mendefinisikan fungsi rekursif di dalam insert

if root is None: return Node(nama, stok, harga) # Jika posisi yang dicapai kosong  maka akan ditempatkan di dalam node kosong itu dan membuat node baru sebagai hasilnya

if stok < root.key: root.left = _ins(root.left) # Jika stok yang dimasukkan lebih kecil dari stok node saat ini, maka produk baru harus masuk ke subtree kiri.

elif stok > root.key: root.right = _ins(root.right) # Jika stok yang dimasukkan lebih besar, produk baru masuk ke subtree kanan. Rekursi terus ke kanan.

else: print(f"Stok {stok} sudah ada ({root.nama}).") # Jika stok sama persis dengan node yang ada, produk ditolak karena BST tidak boleh ada duplikat key. Tampilkan pesan error beserta nama produk yang sudah memakai stok tersebut.

return root # Kembalikan node saat ini agar struktur pohon tetap terhubung dengan benar.

self.root = _ins(self.root) # Hasil akhir rekursi dikembalikan dan disimpan kembali ke self.root

print(f"'{nama}' berhasil ditambahkan.") # Tampilkan konfirmasi bahwa produk berhasil ditambahkan. Baris ini selalu dieksekusi, bahkan saat ada duplikat (karena duplikat hanya mencetak pesan error di dalam rekursi, tidak menghentikan eksekusi).

def search(self, stok): # berfungsi sebagai mencari produk berdasarkan jumlah stok

cur = self.root # Variabel cur adalah penunjuk posisi saat ini dalam pohon.

while cur: # Terus looping selama cur bukan None

if stok == cur.key: return cur # Jika stok yang dicari sama dengan key node saat ini maka node ditemukan

cur = cur.left if stok < cur.key else cur.right # jika stok yang dicari lebih kecil, geser cur ke anak kiri dan jika lebih besar maka geser ke anak kanan. 

def inorder(self, root): membuat fungsi inorder

if root: # Hanya lanjutkan jika node saat ini bukan None

self.inorder(root.left) # kunjungi seluruh subtree kiri terlebih dahulu.

self.inorder(root.right) #  kunjungi seluruh subtree kanan setelah root dicetak. 

def preorder(self, root): #  membuat fungsi preorder

if root:
            print(f"  {root.nama:<20} | Stok: {root.key:<5} | Harga: Rp{root.harga:,}") # mencetak root nya lebih dahulu sebelum turun ke anak anak nya

self.preorder(root.left)
            self.preorder(root.right) # Baru kemudian melakukan rekursi ke kiri lalu kanan.

def postorder(self, root): membuat fungsi postorder

if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(f"  {root.nama:<20} | Stok: {root.key:<5} | Harga: Rp{root.harga:,}") # Kiri dan akan kanan dikunjungi dulu, baru root dicetak di akhir.

def find_min(self): membuat fungsi pencarian minimal dari pohon nya

 cur = self.root # Mulai dari root pohon.

 while cur and cur.left: cur = cur.left # Terus bergerak ke kiri selama masih ada anak kiri

 return cur # Kembalikan node paling kiri yang ditemukan karena  itulah produk dengan stok paling sedikit.

 def find_max(self):
        cur = self.root
        while cur and cur.right: cur = cur.right # sama seperti find_min tapi bergerak ke kanan terus karena Node paling kanan dalam BST memiliki nilai terbesar.

return cur # Kembalikan node paling kanan

def count(self, root):
        return 0 if root is None else 1 + self.count(root.left) + self.count(root.right) # Jika node kosong kembalikan 0. Jika tidak, hitung 1 ditambah jumlah node di subtree kiri ditambah subtree kanan. Hasilnya adalah total seluruh node di pohon.

def total_stok(self, root):
        return 0 if root is None else root.key + self.total_stok(root.left) + self.total_stok(root.right) # Mirip count, tapi yang dijumlahkan bukan 1 melainkan root.key dan Hasilnya adalah penjumlahan stok semua produk di seluruh pohon.

if node: print(f"  {node.nama} | Stok: {node.key} | Harga: Rp{node.harga:,}") # Cek dulu apakah node bukan None, baru cetak. dan digunakan untuk hasil search, find_min, dan find_max.

def main():
    toko = BST() # Membuat objek BST baru bernama toko

while True:#  program terus berjalan sampai pengguna memilih opsi keluar

print("\n=== TOKO SEMBAKO ===")
        print("1. Tambah produk")
        print("2. Cari produk")
        print("3. Tampilkan (urut stok naik)")
        print("4. Tampilkan preorder")
        print("5. Tampilkan postorder")
        print("6. Stok paling sedikit")
        print("7. Stok paling banyak")
        print("8. Total produk & stok")
        print("9. Keluar") # Menampilkan menu pilihan setiap iterasi loop.

try: pilih = int(input("Pilih: "))
        except ValueError: print("Input tidak valid!"); continue # Mencoba mengubah input pengguna menjadi integer. Jika gagal (misalnya pengguna mengetik huruf), tangkap error ValueError, cetak pesan, lalu continue untuk kembali ke awal loop tanpa crash.

if pilih == 1:
            nama = input("Nama produk : ") # Minta input nama produk dari pengguna

try:
                stok  = int(input("Stok        : "))
                harga = int(input("Harga (Rp)  : ")) # Minta input stok dan harga, konversi ke integer

toko.insert(nama, stok, harga)
            except ValueError: print("Stok/harga harus angka!") # Jika pengguna memasukkan bukan angka, tangkap error dan tampilkan pesan.

elif pilih == 2:
            try:
                stok = int(input("Cari stok: "))
                h = toko.search(stok) # Minta input stok yang dicari, lalu panggil search

elif pilih == 3:
            print("-- Urut Stok Naik --")
            toko.inorder(toko.root) if toko.root else print("Belum ada produk.") # Cek dulu apakah pohon tidak kosong Jika ada isinya, panggil inorder mulai dari root

elif pilih == 8:
            print(f"Total produk : {toko.count(toko.root)}")
            print(f"Total stok   : {toko.total_stok(toko.root)} unit") # Memanggil count dan total stok mulai dari root

elif pilih == 9:
            print("Program selesai."); break # Cetak pesan, lalu break untuk keluar dari while True dan mengakhiri program. 


<img width="308" height="345" alt="Screenshot 2026-05-19 000603" src="https://github.com/user-attachments/assets/ce0e637f-bca8-48b2-8641-79921a9cd3d6" />

jika memilih no 1 maka kita diminta menginputkan nama barang, stok, dan harganya berapa dan akan menyimpan ke dalam pohon. jiika memilih 2 user akan diminta menginputkan jumlah stok yang sebelumnya disimpan, kalau ditemukan maka akan menampilkan setail barangnya. jika memilih 3 maka akan menampilkan daftar barang yang sudah dimpan sebelumnya. jika memilih 4 maka akan menampilkan preorder dari barang barang yang kita simpan sebelumnya. jka memilih 5 maka akan menampilkan posterder dari data yang kita simpan sebelumnya. jika memilih 6 maka sitem akan mencari stok yang paling sedikit dari daftar stok yang tersedia. jika memilih 7 maka akan menampilkan jumlah stok yang paling banyak yang ada di daftar barang stok yang ada. jika memilih 8 akan menjumlahkan total stok yang ada ada dalam penyimpanan kita. dan yang terakhir itu no 9 itu berfungsi menghentikan progam yang kita jalankan.

link youtube : https://youtu.be/a1SkDCEfwQM?si=wzil5Lpuu1yyTMcT
