import os

myBook = ['Matlab','Matematika Terpadu','Analisis Numerik','Struktur Data dan Algoritma']
borrowBook = []

def title():
    ttl = "\t~~~perpustakaan jaya abadi~~~\n"
    print(ttl.upper())

def cariBuku(namaBuku):
    kondisi1=True
    kondisi2=True
    for i in range (len(myBook)):
        if(namaBuku.title()==myBook[i]):
            kondisi1=False
            break
            
    if kondisi1 == False:
        print('Buku ' + namaBuku.title() + ' telah ditemukan')
        print("Tekan \"Enter\" untuk melanjutkan")
        x = input()
        menuUtama()
    else:
        for i in range (len(borrowBook)):
            if(namaBuku.title()==borrowBook[i]):
                kondisi2=False
                break
        
    if kondisi2 == False:
        print('Buku ' + namaBuku.title() + ' sedang dipinjam')
        print("Tekan \"Enter\" untuk melanjutkan")
        x = input()
        menuUtama()
    else:
        print('Buku ' + namaBuku.title() + ' tidak ditemukan')
        print("Tekan \"Enter\" untuk melanjutkan")
        x = input()
        menuUtama()
    

def tambahBuku(judulBuku):
    myBook.append(judulBuku.title())

def pinjamBuku(judulBuku):
    kondisi3 = True
    for i in range (len(myBook)):
        if(judulBuku.title()==myBook[i]):
            kondisi3=False
            break
    if kondisi3 == False:
        myBook.remove(judulBuku.title())
        borrowBook.append(judulBuku.title())
    else:
        print('Buku ', judulBuku.title(), 'tidak ditemukan di list')
        print("Tekan \"Enter\" untuk melanjutkan")
        x = input()

def pengembalianBuku(judulBuku):
    kondisi4 = True
    for i in range (len(borrowBook)):
        if(judulBuku.title()==borrowBook[i]):
            kondisi4=False
            break
    if kondisi4 == False:
        myBook.append(judulBuku.title())
        borrowBook.remove(judulBuku.title())
    else:
        print('Buku ', judulBuku.title(), 'tidak sedang dipinjam')
        print("Tekan \"Enter\" untuk melanjutkan")
        x = input()

def denda (hari):
    rasioDenda = 700.0
    bayarDenda = hari*rasioDenda
    print("Biaya yang harus dibayar: Rp",bayarDenda)
    print("Tekan \"Enter\" untuk melanjutkan")
    x = input()

def menuUtama():
    pilihanMenu = ("Cari buku", "Tambah buku", "Pinjam buku","Pengembalian buku","Kalkulator denda")
    #Program akan melakukan perulangan sampai exit
    while(True):
        os.system('cls') #membersihkan layar
        title()
        print('List Buku: ', myBook)
        print('Buku yang sedang dipinjam: ', borrowBook,'\n')
        print("""Selamat Datang di program Katalog Perpustakaan:
        1. {0}
        2. {1}
        3. {2}
        4. {3}
        5. {4}
        9. Keluar""".format(pilihanMenu[0], pilihanMenu[1], pilihanMenu[2],pilihanMenu[3],pilihanMenu[4]))

        choose = eval(input("Masukan Pilihan: "))

        if choose == 1:
            judulBuku = input('Masukkan judul buku: ')
            cariBuku(judulBuku)
        elif choose == 2:
            judulBuku = input('Masukan judul buku: ')
            tambahBuku(judulBuku)
        elif choose == 3:
            judulBuku = input('Masukan judul buku: ')
            pinjamBuku(judulBuku)
        elif choose == 4:
            judulBuku = input('Masukan judul buku: ')
            pengembalianBuku(judulBuku)
        elif choose == 5:
            hari = eval(input('Durasi telat pengembalian\hari : '))
            denda(hari)
        elif choose == 9:
            print('Program Telah Berakhir')
            quit()
        else:
            print('Invalid Input')
            print("Tekan \"Enter\" untuk melanjutkan")
            x = input()

#Program dijalankan
while(True):
    try:
        menuUtama()
    except NameError:
        print("Invalid Input")
        print("Tekan \"Enter\" untuk melanjutkan")
        x = input()
