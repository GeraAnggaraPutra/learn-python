# tipe data string
vr = "Learn python"
print(vr)
txt = "Teks ini akan dipecah\nke dalam 2\t baris" # \n pindah baris \t untuk tab
print(txt)
txt = '''Teks ini
akan dipecah
ke dalam 3 baris'''
print(txt) 
tx1 = 'Belajar '
tx2 = 'python'
hasil = tx1 + tx2
print(hasil)
txt = "Indonesia"
print(txt[0])
print(txt[4])
print(txt[5:9])
print("===============================================")

# tipe data integer
vr = 170
print(vr)
print("===============================================")

# tipe data float
vr = 99.60
print(vr)
a = 3e2 # penulisan notasi ilmiah
b = 3e-2 # penulisan notasi ilmiah
c = 1.34E5 # penulisan notasi ilmiah
print(a)
print(b)
print(c)
print("===============================================")

# tipe data complex number
vr = 4j
print(vr)
print("===============================================")

# tipe data boolean
vr = True
print(vr)
vr = False
print(vr)
vr = 12 < 10
print(vr)
print(12 < 10)
print("===============================================")

# tipe data list
vr = ["satu", "dua", 3, True, 00.9]
print(vr)
vr[0] = "one"
vr[2] = False
print(vr)
print(vr[2:5])
print(vr[:2])
print(vr[2:])
print(vr[:])
print("===============================================")

# tipe data tuple (tidak bisa diubah/diganti setelah didefinisikan)
vr = ("satu", "dua", 3, True, 00.9)
print(vr)
print(vr[2:5])
print(vr[:2])
print(vr[2:])
print(vr[:])
print("===============================================")

# tipe data set (tidak ber-index dan hanya bisa menerima anggota dengan nilai yg berbeda)
vr = {"satu", "dua", "tiga", "dua"}
print(vr)
tx1 = { 1,2,3,4,5 }
tx2 = { 3,4,5,6,7 }
print(tx1 | tx2) # union (operasi gabungan himpunan)
print(tx1 & tx2) # intersection (operasi irisan himpunan)
print("===============================================")

# tipe data dictionary
vr = {"satu":1, "dua":2.1, 3:"tiga", "empat":True}
print(vr)
vr = {
    1: "Learn",
    2: ["Python", "Pascal", "C"],
    "sukses": True,
    "year": 2023,
    "riwayat_sekolah": {
        "SD": "SDN xxxxxx",
        "SMP": "SMP xxxxxx",
        "SMK": "SMK Assalaam"
    }
}
print(vr)
print(vr["riwayat_sekolah"])
vr["year"] = 2024 # mengubah
print(vr["year"])
vr["cita_cita"] = "Programmer" # menambahkan
print(vr)
del vr[1] # menghapus
print(vr)
vr = dict ( # menggunakan constructor dict()
    kegiatan = "Belajar python",
    belajar = "Tipe data",
    hasil = "Bisa!"
)
print(vr)