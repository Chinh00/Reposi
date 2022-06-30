


from cmath import sqrt
from pickle import TRUE


n = int(input("Nhap vao n: "))
def isPrime(n):
    i = 2
    while i < n:
        if n % i == 0:
            return False
        i += 1
    return True
if isPrime(n) == True: print(n, " la so nguyen to.")
else: print(n, " khong phai la so nguyen to") 