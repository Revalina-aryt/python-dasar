# ----------0+++++++++++5-----------8++++++++11-----------
inputUser = float(input('masukan angka yang bernilai\nlebih besar dari 0\natau kurang dari 5\natau lebih besar dari 8\natau kurang dari 11:\n'))
# ----------0+++++++++++
hiji = (inputUser > 0)
print("Lebih dari 0 =", hiji)

# +++++++++++5-----------
dua = (inputUser < 5)
print("Kurang dari 5 =", dua)

# -----------8++++++++
tilu = (inputUser > 8)
print("Lebih dari 8 =", tilu)

#++++++++11-----------
opat = (inputUser < 11)
print("Kurang dari 11 =", opat)

# ----------0+++++++++++5-----------8++++++++11-----------
isCorrect = (hiji and dua) or (tilu and opat)
print("angka yang anda masukan: ", isCorrect)


# ++++++++++0-----------5+++++++++++8--------11+++++++++++
inputUser = float(input('masukan angka yang bernilai\nkurang dari 0\natau lebih besar dari 5\natau kurang dari 8\natau lebih besar dari 11:\n'))

# ++++++++++0-----------
lima = (inputUser < 0)
print("Kurang dari 0 =", lima)

#-----------5+++++++++++
genep = (inputUser > 5)
print("Lebih dari 5 =", genep)

#+++++++++++8--------
tujuh = (inputUser < 8)
print("Kurang dari 8 =", tujuh)

#--------11+++++++++++
dalapan = (inputUser > 11)
print("Lebih dari 11 =", dalapan)

# ++++++++++0-----------5+++++++++++8--------11+++++++++++
isCorrect = (lima and genep) or (tujuh and dalapan)
print("angka yang anda masukan: ", isCorrect)

