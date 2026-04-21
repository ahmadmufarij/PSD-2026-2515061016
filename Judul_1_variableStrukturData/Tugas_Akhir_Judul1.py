import datetime

produk = []

def tambah():
    n = len(produk) + 1
    p = {"kode":f"P{n:02d}", "nama":input("Nama: "), "harga":float(input("Harga: ")),
         "stok":int(input("Stok: ")), "sat":"pcs"}
    produk.append(p)
    print(f"✓ {p['nama']} ({p['kode']})")

def tampil():
    if not produk: return print("Kosong")
    print("\nKODE NAMA      HARGA   STOK")
    print("-"*25)
    for p in produk:
        flag = " ⚠" if p["stok"]<=3 else ""
        print(f"{p['kode']:>3} {p['nama'][:10]:<10} {p['harga']:>7,} {p['stok']:>4}{flag}")

def cari(kw):
    for p in produk:
        if kw.lower() in p['nama'].lower() or p['kode']==kw.upper():
            print(f"{p['kode']} {p['nama']} Rp{p['harga']:,} stok:{p['stok']}")

def stok(kode, jml, op):
    for p in produk:
        if p['kode']==kode:
            if op=="+": p['stok']+=jml
            else: 
                if jml>p['stok']: return print("Stok kurang!")
                p['stok']-=jml
            print(f"{p['nama']}: stok={p['stok']}")
            return
    print("Kode salah!")

while True:
    print(f"\nbarang ({len(produk)} item) 1.Tambah 2.Lihat 3.Cari 4.Stok 5.Menipis 0.Exit")
    c = input("Pilih: ")
    
    if c=='1': tambah()
    elif c=='2': tampil()
    elif c=='3': cari(input("Cari: "))
    elif c=='4':
        kode = input("Kode: ").upper()
        op = input("+/-(tambah/kurang): ")
        stok(kode, int(input("Jml: ")), op)
    elif c=='5':
        tipis = [p for p in produk if p['stok']<=3]
        print("Menipis:", [f"{p['kode']}{p['stok']}" for p in tipis] or "None")
    elif c=='0': break