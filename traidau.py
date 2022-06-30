a = int(input("A = "))
b = int(input("B = "))
c = int(input("C = "))
d = [a, b, c]

print("Co cap so trai dau" if max(d) >= 0 and min(d) < 0 else "Khong co cap so trai dau")

