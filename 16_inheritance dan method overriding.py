# ----------------- INHERITANCE ------------
# class Parent --> class child
# mengakses parent menggunakan super()
# hanya class parent dg hak akses public-protected yg dapat diakses class child
# pengelompokan bermacam class child kedalam class parent mempermudah ketika ada perubahan/perbaikan
# Keuntungan: hemat penulisan variabel, variabel child tinggal ngikut parent
#             semua variabel Program bisa dikumpulkan di parent 

# ---------------- METHOD OVERRIDING ---------------
# child mengambil method dari parent, kemudian memanipulasinya menjadi method baru
# ===================================================
class Person:
    def __init__(self, nama='aris', umur=36):
        self.__nama = nama
        self.__umur = umur
    
    def get_name(self):
        return self.__nama
    def get_umur(self):
        return self.__umur
    def bro(self):
        return 'Nama saya adalah '+ self.__nama + ' dan umur ' + str(self.__umur) + ' tahun'

# Student() , menjadikan Person() sbg parent
# Menjadikan Student() memiliki semua apa yg dimiliki Person()
class Student(Person):
    def __init__(self, nama='noname', umur=0): # constructor default dari Student()
        super().__init__(nama=nama, umur=umur) # super()-> memanggil constructor parentnya

# Selain mewarisi var dari parent, child bisa juga menambahkan var untuk dirinya dan memanipulasi var yang dipanggilnya dari parent
class Teacher(Person):
    def __init__(self, nama='noname', umur=0, id='s000'): # menambahkan param baru selain param dari parent
        super().__init__(nama=nama, umur=umur) 
        self.__id = id
    def perkenalan(self): # --> method override / manipulasi bro()
        return super().bro() + ' memiliki id ' + str(self.__id)

def main():
    s = Student('fahmi', 56) # memiliki parameter seperti parent
    t = Teacher('Dery,s.pd', 56, 's001' ) # param parent + paren child
    
    print(s.bro()) # Nama saya adalah fahmi dan umur 56 tahun
    print(t.perkenalan()) # Nama saya adalah Dery,s.pd dan umur 56 tahun memiliki id s001 

main()



