import math # Agar dapat menggunnakan pi dalam operator math

print('\nLogin')
nama = input('Masukan nama  : ')
nim = input('Masukan NIM   : ') 
prodi = input('Masukan prodi : ') 
print(f'\nData pengguna\n{nama}\n{nim}\n{prodi}') # Menginput nama, nim, prodi, dan menampilkannya dengan print format

print('='*40)

print(f'Selamat datang {nama}, selamat menghitung!!') # Ucapan selamat datang dengan print format

print('='*40)
print('Temukan jawabanmu di sini!!')
print(' a. Bola')
print(' b. Tabung')
print(' c. Limas segitiga')
print('='*40) # Menampilkan menu utama

bangun_ruang = input('Mau ngitung bangun ruang apa nih?? (a/b/c): ') # Menginput bangunan yang volumenya ingin dihitung


if bangun_ruang == 'a':
    jari_jari = float(input('Masukan jari-jari bola: '))
    if jari_jari <= 0 : # Jika jari jari yang dimasukan negatif maka teks dibawah akan muncuk
        print('Tidak ada jari-jari yang negatif atau nol, mulai ulang programnya')
    else:
        volume = (4/3) * math.pi * (jari_jari ** 3) # Rumus bola
        print(f'Bola dengan jari jari {jari_jari} cm memiliki volume sebesar {volume:.2f} kubik satuan')
    
elif bangun_ruang == 'b' :
    tinggi = float(input('Masukan tinggi tabung: '))
    jari_jari = float(input('Masukan jari-jari: ')) 
    if jari_jari <= 0 or tinggi <= 0 : # Jika jari jari yang dimasukan negatif maka teks dibawah akan muncuk
        print('Tidak ada jari-jari dan tinggi yang negatif atau nol, mulai ulang prohramnya')
    else:
        volume = math.pi * (jari_jari * 2) * tinggi # Rumus tabung
        print(f'Tabung dengan tinggi {tinggi} cm dan jari-jari {jari_jari} cm, memiliki volume sebesar {volume:.2f} kubik satuan')

elif bangun_ruang == 'c' :
    tinggi_segitiga = float(input('Masukan tinggi segitiga: '))
    alas_segitiga = float(input('Masukan alas segitiga: '))
    if tinggi_segitiga <= 0 or alas_segitiga <= 0: # Jika jari jari yang dimasukan negatif maka teks dibawah akan muncuk
        print('Tidak ada tinggi dan alas yang negatif atau nol, mulai ulang programmnya')
    else:
        luas_alas = (1/2) * alas_segitiga * tinggi_segitiga
    tinggi_limas = float(input('Masukan tinggi tabung: '))
    if tinggi_limas <= 0 : # Jika jari jari yang dimasukan negatif maka teks dibawah akan muncuk
        print('Tidak ada tinggi kurang dari 1, mulai ulang progammnya')
    else:
        volume = (1/3) * luas_alas * tinggi_limas # Rumus limas segitiga
    
    print(f'Limas segitiga dengan tinggi segitiga {tinggi_segitiga} cm dan alas segitiga {alas_segitiga} cm, memiliki volume sebesar {volume:.2f} cm kubik satuan')
    
else:
    print('Yang kamu masukin kayanya salah deh, coba cek lagi!!') # Jika menginput selain (a, b, c) maka teks tersebut akan keluar
