import os


os.system("cls")


a, b = input("Nhập vào 2 số a và b: ").split()


def f(a):
    arr = []
    for j in range(len(list(a))):
        c = list(a).copy()
        c.pop(j)
        arr.append(int(''.join(c)))
    return str(max(arr))


i = 0
while i < int(b):
    i = i + 1
    a = f(a)
print(a)
