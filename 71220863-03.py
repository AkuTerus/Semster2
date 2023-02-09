# hitung upah dan pajak 
hariKerja = int(input('Masukan hari Kerja : '))
upahBruto = hariKerja*8*10000
pajak = upahBruto*5/100
upahNett = upahBruto-pajak
print(f'Upah karyawan sebelum pajak: Rp {round(upahBruto)}')
print(f'Pajak yang harus di bayar: Rp {round(pajak)}')
print(f'Penghasilan Bersih yang diterima: Rp {round(upahNett)}')