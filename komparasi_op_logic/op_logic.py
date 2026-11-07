# operasi logika atau bolean

# not, or, and, xor

print('====NOT====')
a = True
c = not a
print('data a =',a)
print('------------- NOT')
print('data c =',c)

# OR (jika salah satu true,maka hasilnya adalah true kayak pertambahan)
print('====OR====')
a = False
b = False
c = a or b
print(a,'OR',b,'=',c)
print('====OR====')
a = False
b = True
c = a or b
print(a,'OR',b,'=',c)
print('====OR====')
a = True
b = False
c = a or b
print(a,'OR',b,'=',c)
print('====OR====')
a = True
b = True
c = a or b
print(a,'OR',b,'=',c)

# AND (jika dua buah nilai true, maka hasil true kayak perkalian)
print('====AND====')
a = False
b = False
c = a and b
print(a,'AND',b,'=',c)
print('====AND====')
a = False
b = True
c = a and b
print(a,'AND',b,'=',c)
print('====AND====')
a = True
b = False
c = a and b
print(a,'AND',b,'=',c)
print('====AND====')
a = True
b = True
c = a and b
print(a,'AND',b,'=',c)

# XOR (akan true jika salah satunya true, sisanya false)
print('====XOR====')
a = False
b = False
c = a ^ b
print(a,'XOR',b,'=',c)
print('====XOR====')
a = False
b = True
c = a ^ b
print(a,'XOR',b,'=',c)
print('====XOR====')
a = True
b = False
c = a ^ b
print(a,'XOR',b,'=',c)
print('====XOR====')
a = True
b = True
c = a ^ b
print(a,'XOR',b,'=',c)