# --------  ENCAPSULATION  -------------
# Tujuan :
# - membatasi hak akses pada anggota/member dari sebuah class
# - Memastikan bahwa nilai yang masuk dalam class adalah valid

# Access Modifier di dalam python:
# - public : tanpa underscore
# - private : dengan 2 underscore ( __ )
# - protected : dengan 1 underscore ( _ )

# getter / accessor : method yang digunakan untuk MENGAKSES field dari sebuah class
# setter / mutator : method yang digunakan untuk MENGUBAH field dari sebuah class
# 
# ENCAPSULATION = class yang menggunakan setter dan getter untuk komunikasi dengan objek luar
# ---------------------------------

class Person:
    #umur = 5 #--> public, bisa diakses di fungsi luar dengan p.umur
    __name = 'andi'
    __umur = 5 #--> private, tidak bisa di akses dari luar
               #--> untuk mengakses dan re-value private field, diperlukan - getter & setter
    def get_name(self):
        return self.__name
    def get_umur(self): # --> getter : agar objek dari luar bisa mendapatkan nilai class person.__umur
        return self.__umur

    def set_umur(self, umur): # --> setter : agar objek dari luar bisa memberikan nilai baru pada class person.__umur
                              # --> setter dibuat ketika getter membutuhkan ekspresi/syarat tertentu, contoh: umur, syarat > 0 
                              # --> setter tidak perlu ada jika getter tidak membutuhkan syarat tertentu, contoh: nama
        self.__umur = umur if umur >= 0 else 0

def main():
    p = Person()
    p.set_umur(-12)
    print(p.get_name())
    print(p.get_umur()) # hasil 0 karena tidak sesuai setter

main()



# --------  CONSTRUCTOR -------------
# Method khusus yang bernama sama dengan class dan dipanggil pertama kali ketika kita membuat objek dari suatu class

class Person2:
    # __name = 'andi' #--> depreceated, dipindah jadi parameter constructor
    # __umur = 5

    def __init__(self, name, umur): #----> CONSTRUCTOR: dipanggil pertama kali
        self.__name = name          #----> Jika ada objek dari luar memanggil Person2, maka __init__ yang akan dipanggil
        self.__set_umur(umur)

    def get_name(self):
        return self.__name
    def get_umur(self): 
        return self.__umur

    def __set_umur(self, umur): # di private agar tidak bisa diakses dari luar
                                # pengolahan dialihkan di constructor

        self.__umur = umur if umur >= 0 else 0

# Function menampilkan nama dan umur
def main():
    p = Person2('aris', 36)
    
    # p.set_umur(3) # --> pemrosesan setter di handle constructor
                    # --> objek dari luar tidak bisa lagi mengubah2 seter
    print(p.get_name())
    print(p.get_umur())

main()