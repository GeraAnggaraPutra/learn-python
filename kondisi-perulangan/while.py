i = 1
while i <= 5:
    print('Angka',i)
    i += 1

i = 5
while i >= 1:
    print('Angka',i)
    i -= 1

i = 1
while i <= 7:
    print('Angka',i)
    i += 3

i = 1
while i <= 10:
    if i == 5:
        break
    print(i,'x',i,'=',i*i)
    i += 1

i = 1
while i <= 10:
    i += 1
    if i == 5:
        continue
    print(i,'x',i,'=',i*i)
