s = input("Nhập vào dãy: ")

d = {}
i = 0
while i < len(s):
    d.update({f"{s[i]}" : 0})
    i += 1
i = 0
while i < len(s):
    if (s.count(s[i]) > 0 and d[f"{s[i]}"] == 0):
        d.update({f"{s[i]}": s.count(s[i])})
    i += 1
for x, y in d.items():
    print(f"Ky tu {x} xuat hien {y} lan.")