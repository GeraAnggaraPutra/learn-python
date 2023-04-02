# operator identitas
# is	Bernilai True jika kedua operand merujuk ke object yang sama dan berisi nilai yang sama
# is not	Bernilai True jika kedua operand merujuk ke object yang tidak sama
a = 5
b = 5
c = 6
print('a is b :', a is b)
print('a is c :', a is c)
print('a is not c :', a is not c)
print('\n')
  
i = 'Duniailkom'
j = 'Duniailkom'
print('i is j :', i is j)
print('i is not j :', i is not j)
print('\n')
  
x = ['a','b','c']
y = ['a','b','c']
print('x is y :', x is y)
print('x is not y :', x is not y)

# operator keanggotaan
# in	Bernilai True jika nilai yang dicari ada di dalam himpunan
# not in	Bernilai True jika nilai yang dicari tidak ada dalam himpunan

foo = 'helloworld'
print('foo :',foo)
print('\'o\' in foo     :', 'o' in foo)
print('\'k\' not in foo :', 'k' not in foo)
print('\'d\' not in foo :', 'd' not in foo)
print('\n')
 
 
bar = ['a','b','c']
print('bar :',bar)
print('\'a\' in bar     :', 'a' in bar)
print('\'a\' not in bar :', 'a' not in bar)
print('\'d\' not in bar :', 'd' not in bar)
print('\n')
 
baz = (12,43,102,55)
print('baz :',baz)
print('102 in baz     :', 102 in baz)
print('102 not in baz :', 102 not in baz)
print('35 not in baz  :', 35 not in baz)