a = int(input("A = "))
b = int(input("B = "))
c = int(input("C = "))
print("Cung tinh chan le" if a % 2 == b % 2 == c % 2 == 1 or a %
      2 == b % 2 == c % 2 == 0 else "Khac tinh chan le")
