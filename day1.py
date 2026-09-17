import time
start_time = time.time()
print("hello world 09/09/2026")
# ini adalah contoh komen
"""ini adalah komen multiline
kayak gini dah intinya"""
a = 10 + 6
print(a)
# kita bisa mengcompile pyton ke yg namanya bytecode
# cara mengcompile, buka terminal dan tuliskan
# python -m py_compile day1.py

print(time.time() - start_time, "detik")

# Variabel adalah tempat menyimpan data
# menaruh/assigment nilai
a = 10
x = 5
panjang = 1000

#pemanggilan petama
print("Nilai a =", a)
print("Nilai x =", x)
print("Nilai panjang =", panjang)

#penamaan
nilai_y = 15 #variabel jgn pake underscore
juta10 = 10000000
nilaiz = 17.5

#pemanggilan kedua
print("Nilai a =", a)
#misalkan value a dirubah
a = 7
print("Nilai a =", a)#valuenya dipakai yang terakhir bukan yang diawl

#assignment indirect (secara gak lgsg)
b = a
print("Nilai b =", b)
