nilai = 87

if nilai >= 80:
    print('Selamat, anda lulus dengan nilai', nilai)
else:
    print('Maaf, silahkan coba lagi tahun depan')

nilai = 'C'

if nilai == 'A':
    print('Pertahankan')
elif nilai == 'B':
    print('Tingkatkan')
elif nilai == 'C':
    print('Perbanyak belajar')
elif nilai == 'D':
    print('Jangan keseringan main')
else:
    print('Maaf, format nilai tidak sesuai')

nilai = 55
print('Nilai :',nilai)
if nilai >= 90:
    print('Pertahankan')
elif nilai >= 80 and nilai < 90:
    print('Tingkatkan')
elif nilai >= 70 and nilai < 80:
    print('Perbanyak belajar')
elif nilai < 70:
    print('Jangan keseringan main')
else:
    print('Maaf, format nilai tidak sesuai')