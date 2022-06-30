a = {}
def f(n):
	if (n == 1):
		return 1
	if a.get(n) == None:
		a[n] = (f(n - 1) + 2) % n + 1
n = int(input())
f(n)

# k = int(input())

print("The chosen place is ", a[n])
# Python code for Josephus Problem


# def josephus(n, k):

# 	if (n == 1):
# 		return 1
# 	else:
# 		return (josephus(n - 1, k) + k-1) % n + 1

# n = 14
# k = 2

# print("The chosen place is ", josephus(n, k))

