angka = [6,2,5,4,4,1]
print (angka)
print(len(angka)) # banyak indek dalam satu list
print(type(angka))

# --------------------- MENGAKSES LIST------------
# mengakses list 
buah = ['mangga', 'apel', 'jeruk', 'nanas', 'salak', 'anggur', 'pepaya']
print(buah[0]) #mangga
print(buah[:3]) # ['mangga', 'apel', 'jeruk'] --> start [0], end [3]--> batas akhir tidak ikut tercetak
print(buah[3:]) # ['nanas', 'salak', 'anggur'] --> start [3], end paling akhir --> tidak ikut tercetak
print(buah[-1]) # pepaya --> mencetak dari belakang
print(buah[-4:-1]) #['nanas', 'salak', 'anggur'] --> end [-1] tidak di cetak
# cek anggota dalam list
if 'jeruk1' in buah:
    print('ya, ada jeruk di daftar buah')


# --------------------- MENGGANTI VALUE LIST------------
# Mengganti value list 
buah[2] = 'jeruk bali'
# Mengganti value list dengan range tertentu
buah[3:5] = ['tomat', 'cherry']
#----------------------------


# --------------------- MENAMBAHKAN ANGGOTA LIST------------
# Menambahkan anggota list diakhir list
buah.append('salak') #['mangga', 'apel', 'jeruk bali', 'tomat', 'cherry', 'anggur', 'pepaya', 'salak']
# Menambahkan anggota list di posisi tertentu
buah.insert(2,'mengkudu') #['mangga', 'apel', 'mengkudu', 'jeruk bali', 'tomat', 'cherry', 'anggur', 'pepaya', 'salak']
#Menggabung satu list dengan list lain
sayur = ['wortel', 'kubis']
buah.extend(sayur)

#-------------------

# --------------------- MENGHAPUS ANGGOTA LIST------------
buah.remove('mangga')
# Menghapus dari index tertentu
buah.pop(3) # Menghapus index ke 3
buah.pop() # Menghapus index terakhir
#atau
del buah[1]
# Mengosongkan list
buah.clear()

# --------------------- LOOP LIST------------
# --- FOR ----
buah = ['mangga', 'apel', 'jeruk']
for x in buah:
    print(x)
# mangga
# apel
# jeruk
#--------- atau
for i in range(len(buah)):
    print(buah[i])

#---WHILE----
i = 0
while i < len(buah):
  print(buah[i])
  i = i + 1

# --------------------- SORT LIST------------
buah.sort() 
# angka.sort() #ascending
angka.sort(reverse = True) #descending



# --------------------- COPY LIST------------
# tidak bisa menggunakan buah1 = buah, karena nilainy akan saling terkait
buah2 = buah.copy()

print(buah2)

#------------------ JOIN LIST -----------------
# selain extend(), bisa  dilakukan join dg cara berikut
number_a = [1,4,3,7,5]
text_a = ['a', 'd', 'f']
numbtext = number_a + text_a
# [1, 4, 3, 7, 5, 'a', 'd', 'f']
print(numbtext)

# append()	Adds an element at the end of the list
# clear()	    Removes all the elements from the list
# copy()	    Returns a copy of the list
# count()	    Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	    Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	    Removes the element at the specified position
# remove()	Removes the item with the specified value
# reverse()	Reverses the order of the list
# sort()	    Sorts the list

#Program sederhana

# Mnentukan jumlah siswa dan nilainya
nilai = []
jumlah_siswa = int(input('Masukkan jumlah siswa:'))
for x in range(jumlah_siswa):
    nilai.append(int(input('Masukkan Nilai:')))
print(nilai)

# Menentukan kondisi nilai tiap index siswa
counter = 0
for i in range(jumlah_siswa):
    if (nilai[i] >= 60):
        counter = counter + 1
print('jumlah siswa dengan nilai diatas KKM' sebanyak, counter)
