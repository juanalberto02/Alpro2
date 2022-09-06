def cekParitas(angka):
    if int(angka) % 2 == 0:
        print(angka, "adalah bilangan genap")
    else :
        print(angka, "adalah bilangan ganjil")

if __name__ == "__main__":
    angka = input("Masukkan angka: ")
    cekParitas(angka)
        