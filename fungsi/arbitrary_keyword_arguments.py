# **
def sambung_kata(**kwargs):
    print(kwargs)
    print(type(kwargs))

sambung_kata(a="Belajar",b="python")

def sambung_kata(**kata):
    for i in kata:
        print(i)

sambung_kata(a="Belajar",b="python")

def sambung_kata(**kata):
    for i in kata.values():
        print(i)

sambung_kata(a="Belajar",b="python")

def sambung_kata(**kata):
    hasil = ""
    for i in kata.values():
        hasil += i + " "
    return hasil

print(sambung_kata(a="Belajar",b="python"))

# menggabungkan argument/parameter biasa , *args, **kwargs (harus berurutan)
def test(var1, var2, *args, **kwargs):
    print(var1)
    print(var2)
    print(args)
    print(kwargs)

test(10, 20, 30, 40, 50, a=60, b=70, c=80)