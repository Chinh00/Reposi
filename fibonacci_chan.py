import math
n = int(input("N = "))

def isPerfectSquare(x):
	s = int(math.sqrt(x))
	return s*s == x



def f(n):
	return isPerfectSquare(5*n*n + 4) or isPerfectSquare(5*n*n - 4)
if n % 2 == 1:
    print("N khong phai la so fibonacci chan")
elif f(n) == True:
    print("N la so fibonacci chan")
else:
    print("N khong phai la so fibonacci chan")
