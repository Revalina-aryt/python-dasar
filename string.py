data = "ini adalah string"
print(data)
print(type(data))

# 1. cara membuat string

'''
    1. dengan menggunakan single quote '...'
    2. dengan menggunakan double quote "..."
'''

data = 'menggunakan single quote'
print(data)

data  = "menggunakan double quote"
print(data)

print('"Halo, apa kabar?"')
print("'Halo, apa kabar?'")
print("ini adalah hari jum'at")

# 2. menggunakan tanda \

# membuat tanda ' menjadi string
print('mari solat jum\'at')
print('g\'day, isnt\'t it?')

# backslash \
print("C:\\user\\ucup") #biar kebaca di kasus ini harus double backslash agar mau jadi string

# tab \t
print("ucup \totong, jauhan") # jadi jauhan

# backspace \b
print("ucup \botong") # jadi deketan 

# newline
print("baris pertama.\nbaris kedua") # LF -> line feed -> linux, macos, unix
print("baris pertama.\rbaris kedua") # CR -> carriage return -> commodore, acorn,lisp
print("baris pertama.\r\nbaris kedua")# CRLF -> line feed carriage return -> dipakai oleh windows

# 3. strinf literal atau raw

# hati-hati
print('C:\new folder') # akan salah pathnya

# menggunakan raw string
print(r'C:\\new folder \t\t\\n') #semuanya akan jadi string di raw ini

# multiline literal string
print("""
Nama : Ucup
Kelas : 3 Sd
""")

# multiline literal string string and RAW
print(r"""
Nama : Ucup
Kelas : 3 Sd\new normal
Website : www.ucup.com/newID
""")

