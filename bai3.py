n = int(input("Nhap N: "))
a, b = [], []
for i in range(n):
    try:
        x = input(f"Nhap gia tri thu {i + 1}: ")
        float(x)
        a.append(float(x))
    except ValueError:
        b.append(x)
print(f"Tong cac phan tu cua A = {sum(a)}")
print("B =", sorted(b, reverse=True))