a, b, c, d = float(input("Do dai A = ")), float(input("Do dai B = ")), float(input("Do dai C = ")), float(input("Do dai D = "))
res = -1
def equalMax(x, y, z):
    global  res
    if abs(x - y) < z < (x + y) and abs(x - z) < y < (x + z) and abs(z - y) < x < (z + y):
        p = (x + y + z) / 2
        res = max(res, (p * (p - x) * (p - y) * (p - z)) ** 0.5)
    else: res = -1
equalMax(a, b , c) if a > 0 and b > 0 and c > 0 else ()
equalMax(a, b , d) if a > 0 and b > 0 and d > 0 else ()
equalMax(a, c , d) if a > 0 and c > 0 and d > 0 else ()
equalMax(b, c , d) if b > 0 and c > 0 and d > 0 else ()
if res !=-1 : print(f"Ket qua = {res:.3f}")
else: print(f"Ket qua = {res}")