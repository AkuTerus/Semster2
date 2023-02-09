# Hitung Selisih waktu jam contoh 20:30 - 19:30
jamMasuk = int(input('Masukan Jam Masuk: '))
menitMasuk = int(input('Masukan Menit Masuk: '))
jamKeluar = int(input('Masukan Jam Keluar: '))
menitKeluar=int(input('Masukan Menit Keluar: '))

if jamMasuk < jamKeluar:
    if menitMasuk < menitKeluar:
        total = ((jamKeluar-jamMasuk)*60 + (menitKeluar-menitMasuk))
    else:
        total = ((jamKeluar-jamMasuk)*60 +(menitKeluar-menitMasuk))
else : 
    if menitMasuk < menitKeluar:
        total = 24*60+((jamKeluar-jamMasuk)*60 + (menitKeluar-menitMasuk))
    else:
        total = 24*60+((jamKeluar-jamMasuk)*60 +(menitKeluar-menitMasuk))



# print(f'selisih waktu antara {jamMasuk}:{menitMasuk} dan {jamKeluar}:{menitKeluar} adalah {total} menit')
print('selisih waktu antara ',str(jamMasuk)+':'+str(menitMasuk),'dan',str(jamKeluar)+':'+str(menitKeluar),'adalah',total,'menit')