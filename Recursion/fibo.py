def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)


ans = fib(5)

print(ans)
