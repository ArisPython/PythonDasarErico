#-----------EXCEPTION-----------------
# error ang muncul ketika program dijalankan, akan menimbulkan program exit
# exception akan ditangani oleh kode python

# Mengeluarkan exception/pesan error -->> raise()
def fungsi(bilangan):
    if bilangan < 0:
        raise ValueError('bilangan tidak boleh negatif')
    return bilangan + 1

# Menangkap exception
# try -> pada kode yang memungkinkan error,
# except-> pesan yang muncul error
# finally -> pesan akan muncul baik ada/tidak ada eror
def main():
    x=int(input('masukkan bilangan'))
    try:
        hasil = fungsi(x)
        print(hasil)
    except ValueError as e:
        print(e)
    finally:
        print('ini finally')


main()