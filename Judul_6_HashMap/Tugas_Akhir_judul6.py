class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashMapSeparateChaining:
    def __init__(self, size=10):
        self.SIZE = size
        self.table = [None] * self.SIZE

    def hash_function(self, key):
        return (key % self.SIZE + self.SIZE) % self.SIZE

    def insert(self, key, value):
        index = self.hash_function(key)
        current = self.table[index]
        while current is not None:
            if current.key == key:
                current.value = value
                return
            current = current.next
        new_node = Node(key, value)
        new_node.next = self.table[index]
        self.table[index] = new_node

    def search(self, key):
        index = self.hash_function(key)
        current = self.table[index]
        while current is not None:
            if current.key == key:
                return current
            current = current.next
        return None

    def remove_key(self, key):
        index = self.hash_function(key)
        current = self.table[index]
        prev = None
        while current is not None:
            if current.key == key:
                if prev is None:
                    self.table[index] = current.next
                else:
                    prev.next = current.next
                return True
            prev = current
            current = current.next
        return False

    def display(self):
        print("\nIsi Hash Table (Separate Chaining):")
        for i in range(self.SIZE):
            print(f"{i}: ", end="")
            current = self.table[i]
            while current is not None:
                print(f"({current.key},{current.value}) -> ", end="")
                current = current.next
            print("NULL")


def main():
    # Key = No Tiket, Value = Plat Nomor
    parkir = HashMapSeparateChaining(size=10)
    print("    SISTEM PARKIR")
    while True:
        print("\n1. Masuk")
        print("2. Keluar")
        print("3. Lihat")
        print("0. Selesai")

        pilih = input("Pilih: ")

        if pilih == "0":
            break

        elif pilih == "1":
            try:
                tiket = int(input("No Tiket: "))
                plat = input("Plat Nomor: ")
                parkir.insert(tiket, plat)
                print(f"Tiket {tiket} - {plat} masuk")
            except ValueError:
                print(" No Tiket harus angka")

        elif pilih == "2":
            try:
                tiket = int(input("No Tiket: "))
                hasil = parkir.search(tiket)
                if hasil:
                    print(f"{hasil.value} keluar, bayar Rp5000")
                    parkir.remove_key(tiket)
                else:
                    print(f"Tiket {tiket} tidak ada")
            except ValueError:
                print(" No Tiket harus angka")

        elif pilih == "3":
            parkir.display()

        else:
            print(" Salah pilih")

if __name__ == "__main__":
    main()