

a = int(input("A = "))
b = int(input("B = "))
c = int(input("C = "))
d = {a, b, c}
print("Xep tang dan: ", end = '')
if len(d) == 2: print(min(d),max(d), end='')
elif len(d) == 1: print(a)
else: print(min(d), a + b + c - max(d) - min(d), max(d))
