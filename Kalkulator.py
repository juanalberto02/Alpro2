def kalkulator(angka1,operasi,angka2):
    while True:
        if operasi == '+':
            print('Hasil', angka1 + angka2)
        elif operasi == '-':
            print('Hasil', angka1 - angka2)
        elif operasi == '/':
            print('Hasil', angka1 / angka2)
        elif operasi == '*':
            print('Hasil', angka1 * angka2)
        else:
            print('Error')
            continue
        break
    return 
operator=input("Masukkan jenis operasi (+,-,*,/) :")
num1=int(input("Masukkan angka pertama :"))
num2=int(input("Masukkan angka kedua :"))
kalkulator(num1,operator,num2)
