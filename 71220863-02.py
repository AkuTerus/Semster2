# hitung nilai fungsi x
import math
nilaiX =(input('Masukan Nilai X : '))

if '/' not in nilaiX:
    nilaiX = int(nilaiX)
else: 
    pecahan = nilaiX.split(('/'))
    m = float(pecahan[0])
    n = float(pecahan[1])
    nilaiX=m/n
rumus = 3*(nilaiX**3) - 12*(nilaiX**2) + 7/15*nilaiX - 22/7
print(f'hasilnya adalah : {rumus}')