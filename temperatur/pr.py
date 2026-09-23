# PR BIKIN RUMUS DARI FAHRENHEIT KE KELVIN
print("=====FAHRENHEIT KE Kelvin=====")
fahrenheit = float(input('Masukan  suhu dalam fahrenheit :'))
celcius = (5/9) * (fahrenheit - 32)
print("suhu dalam celcius",celcius,"celcius")
kelvin = celcius + 273
print("suhu dalam kelvin",kelvin,"kelvin")

# PR BIKIN RUMUS DARI KELVIN KE FAHRENHEIT
print("=====KELVIN KE FAHRENHEIT=====")
kelvinb = float(input('Masukan  suhu dalam kelvin :'))
print("suhu dalam kelvinb",kelvinb,"kelvinb")
celciusb = kelvinb - 273
print("suhu dalam celciusb",celciusb,"celciusb")
fahrenheitb = ((9/5) * celciusb) + 32
print("suhu dalam fahrenheitb",fahrenheitb,"fahrenheitb")




