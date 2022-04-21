import math

def prime_gen(n):
    primes = []
    for i in range(2, n+1):
        if all(i % p != 0 for p in primes):
            primes.append(i)
    return primes

primes = prime_gen(100)
c = 0
for prime in primes:
    c+=(math.sin(math.pi/prime))**2

