def sapa(nama1, nama2):
    print('Hai',nama1,'dan',nama2)
sapa('Gera', 'Jon')

def hitung_luas_segitiga(alas, tinggi):
    luas = (alas * tinggi) /2
    print('Luas segitiga adalah',luas)

hitung_luas_segitiga(3, 5)
hitung_luas_segitiga(6, 8)

# default parameter
def tambah(var1 = 5, var2 = 3):
    return var1 + var2

print(tambah())
print(tambah(4,6))

def pangkat(angka, pangkat = 2):
    hasil = 1
    for i in range(0, pangkat):
        hasil = hasil * angka
    return hasil;

print(pangkat(3))
print(pangkat(5))
print(pangkat(3,3))
print(pangkat(5,4))

# Named parameter / keyword arguments
def pangkat(angka, pangkat = 2):
    hasil = 1
    for i in range(0, pangkat):
        hasil = hasil * angka
    return hasil;

print(pangkat(angka = 4, pangkat = 3))
print(pangkat(pangkat = 4, angka = 5))

def akses_database(address, username, password):
    print("====Database Connection====")
    print("server :",address)
    print("username :",username)
    print("password :",password)

akses_database(username="admin", password="quantum", address="192.167.0.3")