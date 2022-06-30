def uscln(a, b):
    if (b == 0):
        return a
    return uscln(b, a % b)
def bscnn(a, b):
    return int((a * b) / uscln(a, b))
res =  0
tmp = 1
while 1 < 2:
    n = int(input())
    if n < 0:
        break
    res = uscln(res, n)
    tmp = bscnn(tmp, n)
print("Boi so chung nho nhat cua day la: ", tmp)
print("Uoc so chung nho nhat cua day la: ", res)
