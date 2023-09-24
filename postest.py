import math

print('\nSebelum menggunakan operasi Kenalan dulu yuk')
nama = input('Kalo boleh tau, siapa namamu?: ')
nim = input('NIM kamu berapaa nih?: ') 
prodi_angkatan = input('Terakhir deh, dari prodi dan angkatan berapa?: ') 
print(f'\nMaaf banyak tanya yaa, selamat datang \n{nama}\n{nim}\n{prodi_angkatan}\nSelamat menghitung!!')

print('='*25)
print('Temukan jawabanmu di sini!!')
print(' a. Bola')
print(' b. Tabung')
print(' c. Limas segitiga')
print('='*25)

bangun_ruang = input('Mau ngitung bangun ruang apa nih?? (a/b/c): ')


if bangun_ruang == 'a':
    jari_jari = float(input('Masukan jari-jari bola: '))
    volume = (4/3) * math.pi * (jari_jari ** 3)
    print(f"Bola dengan jari jari {jari_jari} cm memiliki volume sebesar {volume} kubik satuan")
    
elif bangun_ruang == 'b' :
    tinggi = float(input('Masukan tinggi tabung: '))
    jari_jari = float(input('Masukan jari-jari: '))
    volume = math.pi * (jari_jari * 2) * tinggi
    print(f"Tabung dengan tinggi {tinggi} cm dan jari-jari {jari_jari} cm, memiliki volume sebesar {volume} kubik satuan")

elif bangun_ruang == 'c' :
    tinggi_segitiga = float(input('Masukan tinggi segitiga: '))
    alas_segitiga = float(input('Masukan alas segitiga: '))
    
    luas_alas = (1/2) * alas_segitiga * tinggi_segitiga
    
    tinggi_limas = float(input('Masukan tinggi tabung: '))
    
    volume = (1/3) * luas_alas * tinggi_limas
    
    print(f"Limas segitiga dengan tinggi segitiga {tinggi_segitiga} cm dan alas segitiga {alas_segitiga} cm, memiliki volume sebesar {volume} cm kubik satuan")
    
else:
    print('Yang kamu masukin kayanya salah deh, coba cek lagi!!')
