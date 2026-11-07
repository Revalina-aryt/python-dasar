# operator bitwise, operasi bine, binary

a = 9
b = 5

#bitwise OR (|)
c = a | b
print('\n========OR=======')
print('nilai :',a,' ,binary :',format(a,'08b'))
print('nilai :',b,' ,binary :',format(b,'08b'))
print('-----------------------------(|)')
print('nilai :',c,' ,binary :',format(c,'08b'))

#bitwise AND (&)
c = a & b
print('\n========AND=======')
print('nilai :',a,' ,binary :',format(a,'08b'))
print('nilai :',b,' ,binary :',format(b,'08b'))
print('-----------------------------(&)')
print('nilai :',c,' ,binary :',format(c,'08b'))

#bitwise XOR (^)
c = a ^ b
print('\n========XOR=======')
print('nilai :',a,' ,binary :',format(a,'08b'))
print('nilai :',b,' ,binary :',format(b,'08b'))
print('-----------------------------(^)')
print('nilai :',c,' ,binary :',format(c,'08b'))

#bitwise NOT (~) (bakalan ngemirror kalo ada yang positif bakalan negatif ataupun sebaliknya)
c = ~a
print('\n========NOT=======')
print('nilai :',a,' ,binary :',format(a,'08b'))
print('-----------------------------(~)')
print('nilai :',c,' ,binary :',format(c,'08b'))
#kalo mau nge flip bisa pake XOR biar jadi positif
print('-----------------------------(^)')
d = 0b0000001001
e = 0b1111111111
print('nilai :',e^d,' ,binary :',format(e^d,'08b'))
# koreksi bang, di NOT bisa pakai & 0xFF untuk ngeflip hasilnya:
c = ~ b
print('\nNilai b:',b,' dalam bntk binary:', format(b, '08b'))
print('---------------------------------------( cara lain )')
print('Nilai c:',c,' dalam bntk binary:', format(c & 0xFF, '08b'))

# shifting (ngegeser - geser)

# shift right (geser kanan)
c = a >> 2
print('\n========>>=======')
print('nilai :',a,' ,binary :',format(a,'08b'))
print('-----------------------------(>>)')
print('nilai :',c,' ,binary :',format(c,'08b'))

# shift left (geser kiri)
c = a << 2
print('\n========<<=======')
print('nilai :',a,' ,binary :',format(a,'08b'))
print('-----------------------------(<<)')
print('nilai :',c,' ,binary :',format(c,'08b'))
