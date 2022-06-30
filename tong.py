import

n = int(input("N = "))
x = n
n = int(n / 2)
sum = long(4 * ((n * (n + 1) * (2 * n + 1)) / 6)) if n % 2 == 0 else 0
print(f"P({x}) = {sum - 10 ** 10000}")
