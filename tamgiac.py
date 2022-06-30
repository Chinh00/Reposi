a = int(input("A = "))
b = int(input("B = "))
c = int(input("C = "))
print("Dung la tam giac" if abs(b - c) < a < b+c and abs(a - c) < b<a+c and abs(a - b) < c < a+b else "Khong phai tam giac")
