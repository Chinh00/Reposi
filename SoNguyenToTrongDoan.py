





from cmath import sqrt
from pickle import TRUE


a = int(input("Nhap vao A: "))
b = int(input("Nhap vao B: "))

def isPrime(n):
    i = 2
    while i < n:
        if n % i == 0:
            return False
        i += 1
    return True
print("Cac so nguyen to trong doan tu A den B la: ")
while a <= b:
    if isPrime(a):
        print(a,"\t")
    a += 1