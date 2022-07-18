
def fib(n):
    if n <= 2:
        return 1
    return fib(n-1) + fib(n-2)

def fib_memotization(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 2:
        return 1
    memo[n] = fib_memotization(n-1, memo)  + fib_memotization(n-2, memo)
    return memo[n]

print(fib_memotization(3))
print(fib_memotization(1000))
# print(fib(7))
# print(fib(8))
# print(fib(50))