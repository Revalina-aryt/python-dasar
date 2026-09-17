# a a= 10, a adalah variabel yang bernilai 10

# tipe data: angka satuan yang gak ada koma adalah integer
data_integer = 11
print("data : ", data_integer)
print("- bertipe : ", type(data_integer))

# tipe data: angka dengan koma (desimal) adalah float
data_float = 1.5
print("data :", data_float)
print("- bertipe : ", type(data_float))

# tipe data: kumpulan karakter adalah string
data_string = "ucup 10"
print("data :", data_string)
print("- bertipe : ", type(data_string))

# tipe data: biner true/false adalah boolean
data_bool = True
print("data :", data_bool)
print("- bertipe : ", type(data_bool))

## tipe data khusus

# bilangan kompleks
data_complex = complex(5,6) # 5 adalah bilangan ril dan 6 adalah bilangan imajiner (i)
print("data :", data_complex)
print("- bertipe : ", type(data_complex))

# tipe data bahasa C

from ctypes import c_double

data_c_double = c_double(10.5)
print("data :", data_c_double)
print("- bertipe : ", type(data_c_double))