import os

myBook = ['Buku1','Buku2','Buku3','Buku4','Buku5']
borrowBook = []

def cariBuku(namaBuku):
    kondisi1=True
    kondisi2=True
    for i in range (len(myBook)):
        if(namaBuku==myBook[i]):
            kondisi1=False
            break
            
    if kondisi1 == False:
        print('Buku ' + myBook[i] + ' telah ditemukan')
        x = input()
    else:
        for i in range (len(borrowBook)):
            if(borrowBook==myBook[i]):
                kondisi2=False
                break
        
    if kondisi2 == False:
        print('Buku ' + myBook[i] + ' sedang dipinjam')
        x = input()
    else:
        print('Buku ' + myBook[i] + ' tidak ditemukan')
        x = input()
    

def tambahBuku(judulBuku):
    myBook.append(judulBuku)
    menuUtama()

def hapusBuku(judulBuku):
    myBook.remove()

def pinjamBuku(judulBuku):
    myBook.remove(judulBuku)
    borrowBook.append(judulBuku)
    menuUtama()

def pengembalianBuku(judulBuku):
    myBook.append(judulBuku)
    borrowBook.remove(judulBuku)
    menuUtama()

def menuUtama():
    #Program akan melakukan perulangan sampai exit
    while(True):
        os.system('cls') #membersihkan layar
        print('List Buku')
        print(myBook)
        print('Buku yang sedang dipinjam')
        print(borrowBook)
        print('\n')
        print("""Selamat Datang di program Katalog Perpustakaan:
        1. {0}
        2. {1}
        3. {2}
        4. {3}
        9. Keluar""".format("Cari buku", "Tambah buku", "Pinjam buku","Pengembalian Buku"))

        choose = eval(input("Masukan Pilihan: "))

        if choose == 1:
            judulBuku = input('Masukkan judul buku : ')
            cariBuku(judulBuku)
        elif choose == 2:
            judulBuku = input('Masukan judul buku : ')
            tambahBuku(judulBuku)
        elif choose == 3:
            judulBuku = input('Masukan judul buku : ')
            pinjamBuku(judulBuku)
        elif choose == 9:
            print('Program telah berakhir')
            break
        else:
            print('Invalid Input')

#Program dijalankan
menuUtama()
