# ---------- OPERATOR OVERLOADING -----------
# Menggunakan SPECIAL METHOD untuk memberikan nilai operator dengan nilai tertentu
# SPECIAL METHOD -->__add__ untuk overload operator'+' pada kasus fungsi()+fungsi()
#                -->__sub__ untuk overload operator'-'
#                -->__mul__ untuk overload operator'*'
#                -->__truediv__ untuk overload operator'/'
#                -->...dll, browsing sendiri

class Person:
    def __init__(self, nama='aris', umur=36):
        self.__nama = nama
        self.__umur = umur
    
    def get_name(self):
        return self.__nama
    def get_umur(self):
        return self.__umur
    def bro(self):
        return 'Nama saya adalah '+ self.__nama + 'dan umur ' + str(self.__umur) + ' tahun'
    
    #--> OPERATOR OVERLOADING
    def __add__(self, other): # other = z, y, __add__ menggantikan '+'
        n = Person(self.get_name() + other.get_name(), self.get_umur() + other.get_umur())
        return n
    def __str__(self): 
        return self.bro()

# fungsi menggabung nama dan umur
def main():
    z = Person('yudi', 45)
    y = Person('fahmi', 34)
    # print(z.bro())

    # cara1: menggunakan  __add__ untuk menggabungkan 2 fungsi, karena z+y ->person() + person() error. nilai '+' artinya ndak jelas
    x = z + y 
    print(x.bro()) # Nama saya adalah yudifahmi dan umur 79 tahun

    # cara2: mengguunakan __str__ ntuk menampilkan penggabungan fungsi sebagai string.
    print(str(x)) # Nama saya adalah yudifahmi dan umur 79 tahun

main()

