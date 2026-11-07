# operasi komparasi

# setiap hasil dari operasi adalah boolean

# >, <, >=, <=, ==, !=, is, is not

a = 4
b = 2

# lebih besar dari >
print('=====lebih besar dari (>)')
hasil = a > 3
print(a,'>',3,'=',hasil)
hasil = b > 3
print(b,'>',3,'=',hasil)
hasil = b > 2
print(b,'>',2,'=',hasil)

# kurang dari <
print('=====kurang dari (<)')
hasil = a < 3
print(a,'<',3,'=',hasil)
hasil = b < 3
print(b,'<',3,'=',hasil)
hasil = b < 2
print(b,'<',2,'=',hasil)

# lebih dari sama dengan >=
print('=====lebih dari sama dengan (>=)')
hasil = a >= 3
print(a,'>=',3,'=',hasil)
hasil = b >= 3
print(b,'>=',3,'=',hasil)
hasil = b >= 2
print(b,'>=',2,'=',hasil)
# lebih dari sama dengan >=
print('=====lebih dari sama dengan (>=)')
hasil = a >= 3
print(a,'>=',3,'=',hasil)
hasil = b >= 3
print(b,'>=',3,'=',hasil)
hasil = b >= 2
print(b,'>=',2,'=',hasil)

# kurang dari sama dengan <=
print('=====kurang dari sama dengan (<=)')
hasil = a <= 3
print(a,'<=',3,'=',hasil)
hasil = b <= 3
print(b,'<=',3,'=',hasil)
hasil = b <= 2
print(b,'<=',2,'=',hasil)

# sama dengan ==
print('=====sama dengan (==)')
hasil = a == 3
print(a,'==',3,'=',hasil)
hasil = b == 3
print(b,'==',3,'=',hasil)
hasil = b == 2
print(b,'==',2,'=',hasil)

# tidak sama dengan !=
print('=====tidak sama dengan (!=)')
hasil = a != 3
print(a,'!=',3,'=',hasil)
hasil = b != 3
print(b,'!=',3,'=',hasil)
hasil = b != 2
print(b,'!=',2,'=',hasil)

# 'is' sebagai komparansi object identity
print('=====object identity (is)')
x = 5 # ini adalah assigment membuat object
y = 5 # kalo beda angka beda id
print('nilai x =,',x,',id = ',hex(id(x)))
print('nilai y =,',y,',id = ',hex(id(y)))
hasil = x is y
print('x is y=',hasil)

# 'is' sebagai komparansi object identity
x = 5 # ini adalah assigment membuat object
y = 6 # kalo beda angka beda id
print('nilai x =,',x,',id = ',hex(id(x)))
print('nilai y =,',y,',id = ',hex(id(y)))
hasil = x is y
print('x is y=',hasil)

# 'isnot' sebagai komparansi object identity
print('=====object identity (is not)')
x = 5 # ini adalah assigment membuat object
y = 5 # kalo beda angka beda id
print('nilai x =,',x,',id = ',hex(id(x)))
print('nilai y =,',y,',id = ',hex(id(y)))
hasil = x is not y
print('x is y=',hasil)

# 'is' sebagai komparansi object identity
x = 5 # ini adalah assigment membuat object
y = 6 # kalo beda angka beda id
print('nilai x =,',x,',id = ',hex(id(x)))
print('nilai y =,',y,',id = ',hex(id(y)))
hasil = x is not y
print('x is y=',hasil)
