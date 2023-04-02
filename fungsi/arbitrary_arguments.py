# *
def sapa(*args):
    print(args)
    print(type(args))

sapa('gera', 'alex', 'jon')

def sapa(*nama):
    for i in nama:
        print("Halo", i)

sapa('alex', 'bow')

def jumlah(*args):
    hasil = 0
    for i in args:
        hasil+= i
    return hasil

print(jumlah(5,7))
print(jumlah(5,7,4,3))
print(jumlah(100,200,50))

# program python untuk mencari nilai rata - rata menggunakan arbitrary arguments
def rata2(*args):
    hasil = 0
    for i in args:
        hasil += i
    return hasil / len(args) # len(args) dipakai untuk menghitung total jumlah argument

print(rata2(5,7))
print(rata2(10,20,30))