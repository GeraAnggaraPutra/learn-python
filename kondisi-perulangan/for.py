warna = ['merah', 'kuning', 'hijau', 'hitam']
for i in warna:
    print(i)
warna = {'merah', 'kuning', 'hijau', 'hitam'}
for i in warna:
    print(i)

nama = 'geraanggara'
for x in nama:
    print(x)

for i in range(5):
    print('range ', i)

for i in range(5,10):
    print('range ', i)

for i in range(3,30,3):
    print(i)

for i in range(1, 11):
    print(i,'x',i,'=',i*i)
    if i == 5:
        break

for i in range(1,11):
    if i == 5:
        continue
    print(i,'x',i,'=',i*i)