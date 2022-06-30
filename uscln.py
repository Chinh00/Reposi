a = int(input("a = "))
b = int(input("b = "))
def uscln(a, b):
    if (b == 0):
        return a
    return uscln(b, a % b)
def bscnn(a, b):
    return int((a * b) / uscln(a, b))
print("Ước số chung lớn nhất của", a, "và", b, "là:", uscln(a, b))
print("Bội số chung nhỏ nhất của", a, "và", b, "là:", bscnn(a, b))
