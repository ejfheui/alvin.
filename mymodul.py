x = 100 #file mymodul

#fungsi
def kali(a, b):
    return a * b

#fungsi mymodul
import mymodul

int(mymodul.x)

hasil = mymodul.kali(4, 7)
print(hasil)

#1
from mymodul import x, kali

print(x)
print(kali(2, 9))
