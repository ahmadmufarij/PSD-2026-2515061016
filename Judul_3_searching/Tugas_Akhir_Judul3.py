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
]

def binary_search(arr, n, target):
    l = 0
    r = n - 1
    pos = - 1
    while l <= r:
        m = l + (r - l) // 2
        print(f"Median: {m}, produk: {arr[m]}")
        if arr[m].lower() == target.lower():
            pos = m
            break
        elif arr[m].lower() < target.lower():
            print("Mencari di kanan")
            l = m + 1
        else:
            print("Mencari di kiri")
            r = m - 1
    return pos

def main():
    n = len(katalog)
    print("Daftar produk (terurut A-Z):")
    for i in range(n):
        print(f"  [{i}] {katalog[i]}")

    target = input("\nMasukkan nama produk yang ingin dicari: ")

    pos = binary_search(katalog, n, target)

    if pos != -1:
        print(f"Produk ditemukan pada indeks ke-{pos}: {katalog[pos]}")
    else:
        print("Produk tidak ditemukan")

if __name__ == "__main__":
    main()