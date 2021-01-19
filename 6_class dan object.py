# cara atau sudut pandang dalam menyelesaikan masalah
class Segitiga:
    alas = 0 #==> field
    tinggi = 0
    def hitungLuas(self): #==> method
        return 0.5 * self.alas * self.tinggi

def main():
    s3 = Segitiga()
    s3.alas = int(input('masukkan alas : ')) #==> object
    s3.tinggi = int(input('masukkan tinggi : '))

    luas = s3.hitungLuas()
    print('luas segitiga : ',luas)

main()