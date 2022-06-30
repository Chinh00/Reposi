a, b = input("Nhập vào 2 số a và b: ").split()

d = [int(a[i]) for i in range(-1, -len(a) - 1, -1)]
for i in range(int(b)):
    d.remove(min(d))
d.reverse()
for x in d: print(x,sep="", end="")