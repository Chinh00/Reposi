n = int(input("n = "))

s = 0
def total(n):
    global s
    if n == 0: return 0
    s += n % 10
    total(n // 10)
total(n)
print(s)