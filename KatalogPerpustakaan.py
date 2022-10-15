myBook = ['Buku1','Buku2','Buku3','Buku4','Buku5']

def cariBuku(namaBuku):
    kondisi1=True
    for i in range (len(myBook)):
        if(namaBuku==myBook[i]):
            kondisi1=False
            break
            
    if kondisi1 == False:
        print("Ada bukunya!")

    else:
        print("Gaada bukunya!")

def tambahBuku(namaBuku,jumlah):
    for i in range (jumlah):
        myBook.append(namaBuku)
    menuUtama()

def pinjamBuku(namaBuku,jumlah):
    for i in range (jumlah):
        myBook.remove(namaBuku)
    menuUtama()

def menuUtama():
    print(myBook)
    print("""Menu Utama:
    1. {0}
    2. {1}
    3. {2}
    9. Keluar""".format("Cari buku", "Tambah buku", "Pinjam buku"))

    input1 = eval(input("Masukan Pilihan: "))

    if input1 == 1:
        input2 = input('Masukkan nama buku : ')
        cariBuku(input2)

    elif input1 == 2:
        input2 = input('Masukan nama buku : ')
        input3 = eval(input('Jumlah buku : '))
        tambahBuku(input2,input3)

    elif input1 == 3:
        input4 = input('Masukan nama buku : ')
        input5 = eval(input('Jumlah buku : '))
        pinjamBuku(input4,input5)

    elif input1 == 9:
        exit

    else:
        print("GOBLOK")

menuUtama()
