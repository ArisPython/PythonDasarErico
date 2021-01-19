# identifier menunjuk ke objek

class Manusia:
    nama = 'no name' # nama-> IDENTIFIER/VARIABLE, 'noname'-> OBJECT/VALUE
    def Copy(self):
        manusiaBaru = Manusia()
        manusiaBaru.nama = self.nama + 'copy'
        return manusiaBaru
    
def main():
    m = Manusia() # object dari class Manusia
    m2 = m.Copy() #--> object dari method copy
    print(m2.nama)



# main()
# class Segitiga:
#     alas = 0 
#     tinggi = 0
#     # objek sederhana (dalam class)
#     # alas, tinggi --> IDENTIFIER / VARIABLE
#     # 0 --> OBJECT / VALUE dengan type data int
#     def hitungLuas(self): 
#         return 0.5 * self.alas * self.tinggi
#     # objek dalam function

# def main():
#     s3 = Segitiga()
#     s3.alas = int(input('masukkan alas : ')) #==> object dari hitungLuas
#     s3.tinggi = int(input('masukkan tinggi : '))

#     luas = s3.hitungLuas()
#     print('luas segitiga : ',luas)

main()