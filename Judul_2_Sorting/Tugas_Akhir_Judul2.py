def tukar(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def bubble_sort(arr, n):
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                tukar(arr, j, j + 1)

def main():
    try:
        n = int(input("Masukkan jumlah jenis barang: "))
    except ValueError:
        print("Input tidak valid!")
        return
    
    arr = []
    print("Masukkan jumlah stok barang:")
    for i in range(n):
        while True:
            try:
                stok = int(input(f"Stok barang ke-{i+1}: "))
                if stok >= 0:
                    arr.append(stok)
                    break
                else:
                    print("Stok tidak boleh negatif!")
            except ValueError:
                print("Input tidak valid, masukkan angka >= 0!")
    
    print(f"\nStok barang sebelum diurutkan: {arr}")
    bubble_sort(arr, n)
    print("Stok barang setelah diurutkan (Bubble Sort):", end=" ")
    for i in range(n):
        print(arr[i], end=" ")
    print()
    print(f"Total stok: {sum(arr)} buah")

if __name__ == "__main__":
    main()