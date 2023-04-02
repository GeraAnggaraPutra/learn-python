def hitung_luas_segitiga(alas, tinggi):
    luas = (alas * tinggi) /2
    return luas

var1 = hitung_luas_segitiga(5, 7)
print('Luas segitiga adalah', var1)

def hitung_luas_segitiga(alas, tinggi):
    return (alas * tinggi) /2

print('Luas segitiga :', hitung_luas_segitiga(5, 7))

def harga_setelah_pajak(harga_dasar):
    return harga_dasar + (harga_dasar * 10/100)

harga_cilok = 5000
harga_final_cilok = harga_setelah_pajak(harga_cilok)
print('Harga cilok Rp.',harga_final_cilok)