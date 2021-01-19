# iterable adalah object yan dapat melakkan iterasi
# konsep iterasi
l = [11,12,13,14]
x = iter(l)
x2 = iter(l)

print(next(x)) #11
print(next(x)) #12
print(next(x)) #13
print(next(x)) #14
# print(next(x)) #error, karena iterasi x hanya sampai [3]
print(next(x2)) #11

# Penerapan iterator ada pada loop
for x in l:
    print(x)

# Iterator juga bisa menggunakan generator
def generator(n):
    i = 0
    while i < n:
        yield i
        i = i+1

for y in generator(5):
    print(y)

#Comprehension Syntax / pemendekan syntax

#contoh: program bilangan ganjil
data=[]
for i in range (11):
    if i % 2 != 0:
        data.append(i)
print(data)
#bisa juga di tulis
data2 = [i for i in range(11) if i % 2 != 0]
print(data2)
# data=[] bisa dihanti () untuk tupple, dan {} untuk dict




