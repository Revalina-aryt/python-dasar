print("=====FAHRENHEIT KE Kelvin=====")
f = float(input('Masukan  suhu dalam fahrenheit :'))
k = (5/9) * (f - 32) + 273
print("suhu f ke k adalah :",k,"kelvin")

print("=====KELVIN KE FAHRENHEIT=====")
k = float(input('Masukan  suhu dalam kelvin :'))
f = (9/5) * (k - 273) + 32
print("suhu k ke f adalah :",f,"fahrenheit")