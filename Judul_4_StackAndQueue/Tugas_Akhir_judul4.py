class StackArray:
    def __init__(self, max_size=100):
        self.MAX = max_size
        self.st = [None] * self.MAX
        self.top_idx = -1

    def is_empty(self):
        return self.top_idx == -1

    def is_full(self):
        return self.top_idx == self.MAX - 1

    def push(self, x):
        if self.is_full():
            print("Stack penuh")
            return
        self.top_idx += 1
        self.st[self.top_idx] = x
        print(f"Push {x} berhasil")

    def pop(self):
        if self.is_empty():
            print("Stack kosong")
            return
        print(f"Pop {self.st[self.top_idx]} berhasil")
        self.top_idx -= 1

    def peek(self):
        if self.is_empty():
            print("Stack kosong")
            return
        print(f"Elemen teratas: {self.st[self.top_idx]}")

    def display(self):
        if self.is_empty():
            print("Stack kosong")
            return
        print("Isi stack (atas ke bawah): ", end="")
        for i in range(self.top_idx, -1, -1):
            print(self.st[i], end=" ")
        print()


def main():
    keranjang = StackArray()
    pilih = 0
    while pilih != 5:
        print("\n TOKO SEDERHANA")
        print("1. Tambah Barang")
        print("2. Hapus Barang Terakhir")
        print("3. Lihat Barang Teratas")
        print("4. Lihat Keranjang")
        print("5. Keluar")
        try:
            pilih = int(input("Pilih: "))
        except ValueError:
            print("Input tidak valid!")
            continue
        if pilih == 1:
                val = input("nama barang: ")
                keranjang.push(val)
        elif pilih == 2:
            keranjang.pop()
        elif pilih == 3:
            keranjang.peek()
        elif pilih == 4:
            keranjang.display()
        elif pilih == 5:
            print("Terima kasih!")
        else:
            print("Pilihan tidak valid!")


if __name__ == "__main__":
    main()