
def gt(a): 
    if a == 1: return 1
    else: return a * gt(a - 1)

s = 0
def fn(n):
    if n == 1: return gt(1)
    s += gt(n)
    fn(n - 1)

n = int(input())
fn(n)
print(fn(6))
