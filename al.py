seq = [0, 1, 2, 3, 5, 8, 13]
result = filter(lambda x: x % 2 != 0, seq)
print(list(result))


result = filter(lambda x: x % 2 == 0, seq)
print(list(result))
