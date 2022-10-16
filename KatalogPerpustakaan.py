import os

myBook = ['Buku1','Buku2','Buku3','Buku4','Buku5']
borrowBook = []
namaPeminjam = []

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

def pinjamBuku(judulBuku,namaPeminjam):
    myBook.remove(judulBuku)
    borrowBook.append(judulBuku)
    namaPeminjam.append(namaPeminjam)
    menuUtama()

def pengembalianBuku(judulBuku,namaPeminjam):
    for i in range (len(borrowBook)):
        if borrowBook[i]==namaPeminjam[i]:
            myBook.append(judulBuku)
            borrowBook.remove(judulBuku)
            namaPeminjam.remove(namaPeminjam)

def menuUtama():
    #Program akan melakukan perulangan sampai exit
    while(True):
        os.system('cls') #membersihkan layar
        print('List Buku')
        print(myBook)
        print('Buku yang sedang dipinjam')
        print(borrowBook)
        print('Nama peminjam')
        print(namaPeminjam)
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
            namaPeminjam = input('Masukan nama peminjam : ')
            pinjamBuku(judulBuku,namaPeminjam)
        elif choose == 9:
            print('Program telah berakhir')
            break
        else:
            print('Invalid Input')

#Program dijalankan
menuUtama()
