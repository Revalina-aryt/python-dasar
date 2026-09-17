# operasi Aritmatika

a = 10
b = 3

# operasi tambah +
hasil = a + b
print(a,'+',b, '=', hasil)

# operasi pengurangan -
hasil = a - b
print(a,'-',b, '=', hasil)

# operasi perkalian *
hasil = a * b
print(a,'x',b, '=', hasil)

# operasi pembagian /
hasil = a / b
print(a,'/',b, '=', hasil)

# operasi eskponen (pangkat) **
hasil = a ** b
print(a,'^',b, '=', hasil)

# operasi modulus (sisa pembagian) %
hasil = a % b
print(a,'%',b, '=', hasil)

# operasi floor division // (dibulatkan kebawah)
hasil = a // b
print(a,'//',b, '=', hasil)

# Prioritas Operasi, operational precedence
'''
1. ()
2. eksponen **
3. perkalian, pembagian, modulus, floor division * ** / % //
4. pertambahan dan pengurangan + -

'''
x = 3
y = 2
z = 4

hasil = x ** y * z + x / y - y % z // x
print(x,'**',y,'*',z,'+',x,'/',y,'-', y, '%',z,'//',x, '=', hasil)

#kurung akan mengambil langkah pertama
hasil = (x + y) * z
print('(',x,'+',y,') *',z, '=', hasil)