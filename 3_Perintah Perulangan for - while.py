#FOR
# - Tentukan var sumber 'data'
# - var i untuk indeks
# range() untuk membuat list

data = 10
for i in range(data):
    print(i)
# Hasilnya 1 - 9
#----------------------


data2 = ['andi', 'rudi','zainal']
for i in (data2):
    print(i)
# andi
# rudi
# zainall
#---------------------------

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)
# red apple
# red banana
# red cherry
# big apple
# big banana
# big cherry
# tasty apple
# tasty banana
# tasty cherry    
#----------------------------

data3 = 4
for i in range(data3):
    for j in range(i):
        print(i, end='')
    print()
# 1
# 22
# 333
#==============================

# ====================== WHILE =====================
# ...Selama variable syarat terpenuhi maka masih tetap dijalankan

# selama 'data' kurang dari 10, maka 'data' akan terus tercetak
# 'data' akan berhenti mencetak setelah bernilai 9
data = 1
while(data < 10):
    print(data)
    data=data+1
# hasil 1-9
#---------------------------

# Menghentikan di tengah perulangan dengan 'break'
data = 1
while(data < 10):
    print(data)
    if data == 3:
        break
    data=data+1
# hasil 1-3
#-----------------------------


# Program luas segi pannjang
# Selama jawab ya, maka program akan berjalan
while(True):
    jawab = str(input('apakah anda ingin menjalankan program: '))
    if jawab == 'ya' or jawab == 'y' or jawab == 'yoi':
        p = float(input('masukkan panjang :' ))
        l = float(input('masukkan lebar:' ))
        Luas = p*l
        print('luas segi panjang adalah: ', Luas)
    else:
        print('anda keluar dari program, terima kasih')
        break
    
# apakah anda ingin menjalankan program: y
# masukkan panjang :5
# masukkan lebar:6
# luas segi panjang adalah:  30.0
# apakah anda ingin menjalankan program: yoi

