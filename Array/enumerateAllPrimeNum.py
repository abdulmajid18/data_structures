from math import sqrt


def enumerateAllPrime(A):
    primes = []
    for i in range(2, A):
        prime = True
        for j in range(2, int(sqrt(i)+1)):
            if (i % j == 0):
                prime = False
        if prime:
            primes.append(i)
        else:
            continue
    return primes


# ans = enumerateAllPrime(18)
# print(ans)

# x = [F,F,T,T,T,T,T,T,T,T,T]
def generate_primes(n):
    primes = []
    is_prime = [False, False] + [True] * (n - 1)
    for p in range(2, n+1):
        if is_prime[p]:
            primes.append(p)
            for i in range(p, n + 1, p):
                is_prime[i] = False
    return primes


ans = generate_primes(18)
print(ans)
