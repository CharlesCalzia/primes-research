import matplotlib.pyplot as plt

def primeGen(n):
    primes = []
    for i in range(2, n+1):
        if all(i % p != 0 for p in primes):
            primes.append(i)
    return primes

def plotPrimes(n):
    plt.plot(primeGen(n))
    plt.show()

plotPrimes(100)