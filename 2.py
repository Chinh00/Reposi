import os
os.system("cls")
s = input("Nhap vao cac xau nhi phan: ").split(", ")
def convert(i):
    s = 0
    x = 0
    for j  in range(-1, -len(i) - 1, -1):
        if i[j] == "0" or i[j] == "1":
            s += int(i[j]) * (2 ** x)
            x += 1
        else: return "Loi"
    return s
print("Gia tri cac chuoi nhi phan vua nhap la: ")
for x in s:
    print(f"{x} => {convert(x)}")
