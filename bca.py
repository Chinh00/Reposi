n = int(input("N = "))
print(f"P({n}) = {sum((x ** 2 for x in range(2, n + 1, 2)))}")