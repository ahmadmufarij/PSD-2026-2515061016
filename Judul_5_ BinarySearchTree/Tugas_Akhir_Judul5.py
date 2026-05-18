class Node:
    def __init__(self, nama, stok, harga):
        self.key = stok
        self.nama = nama
        self.harga = harga
        self.left = self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, nama, stok, harga):
        def _ins(root):
            if root is None: return Node(nama, stok, harga)
            if stok < root.key: root.left = _ins(root.left)
            elif stok > root.key: root.right = _ins(root.right)
            else: print(f"Stok {stok} sudah ada ({root.nama}).")
            return root
        self.root = _ins(self.root)
        print(f"'{nama}' berhasil ditambahkan.")

    def search(self, stok):
        cur = self.root
        while cur:
            if stok == cur.key: return cur
            cur = cur.left if stok < cur.key else cur.right
        return None

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(f"  {root.nama:<20} | Stok: {root.key:<5} | Harga: Rp{root.harga:,}")
            self.inorder(root.right)

    def preorder(self, root):
        if root:
            print(f"  {root.nama:<20} | Stok: {root.key:<5} | Harga: Rp{root.harga:,}")
            self.preorder(root.left)
            self.preorder(root.right)

    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(f"  {root.nama:<20} | Stok: {root.key:<5} | Harga: Rp{root.harga:,}")

    def find_min(self):
        cur = self.root
        while cur and cur.left: cur = cur.left
        return cur

    def find_max(self):
        cur = self.root
        while cur and cur.right: cur = cur.right
        return cur

    def count(self, root):
        return 0 if root is None else 1 + self.count(root.left) + self.count(root.right)

    def total_stok(self, root):
        return 0 if root is None else root.key + self.total_stok(root.left) + self.total_stok(root.right)


def tampil(node):
    if node: print(f"  {node.nama} | Stok: {node.key} | Harga: Rp{node.harga:,}")

def main():
    toko = BST()
    while True:
        print("\n=== TOKO SEMBAKO ===")
        print("1. Tambah produk")
        print("2. Cari produk")
        print("3. Tampilkan (urut stok naik)")
        print("4. Tampilkan preorder")
        print("5. Tampilkan postorder")
        print("6. Stok paling sedikit")
        print("7. Stok paling banyak")
        print("8. Total produk & stok")
        print("9. Keluar")

        try: pilih = int(input("Pilih: "))
        except ValueError: print("Input tidak valid!"); continue

        if pilih == 1:
            nama = input("Nama produk : ")
            try:
                stok  = int(input("Stok        : "))
                harga = int(input("Harga (Rp)  : "))
                toko.insert(nama, stok, harga)
            except ValueError: print("Stok/harga harus angka!")

        elif pilih == 2:
            try:
                stok = int(input("Cari stok: "))
                h = toko.search(stok)
                print("Ditemukan ->"); tampil(h) if h else print("Tidak ditemukan.")
            except ValueError: print("Input tidak valid!")

        elif pilih == 3:
            print("-- Urut Stok Naik --")
            toko.inorder(toko.root) if toko.root else print("Belum ada produk.")

        elif pilih == 4:
            print("-- Preorder --")
            toko.preorder(toko.root) if toko.root else print("Belum ada produk.")

        elif pilih == 5:
            print("-- Postorder --")
            toko.postorder(toko.root) if toko.root else print("Belum ada produk.")

        elif pilih == 6:
            tampil(toko.find_min()) if toko.root else print("Belum ada produk.")

        elif pilih == 7:
            tampil(toko.find_max()) if toko.root else print("Belum ada produk.")

        elif pilih == 8:
            print(f"Total produk : {toko.count(toko.root)}")
            print(f"Total stok   : {toko.total_stok(toko.root)} unit")

        elif pilih == 9:
            print("Program selesai."); break

        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    main()