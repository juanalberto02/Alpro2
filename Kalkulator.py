def checkangka(angka):
    cek = angka.isnumeric()
    return cek

if __name__ == "__main__":
    angka = input("Masukkan angka: ")
    if(checkangka(angka)):
        print("Anda memasukkan angka ",angka)
    else:
        print("Masukkan angka!")
