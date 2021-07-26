from math import sqrt, floor

def isPrime(n):
    if n > 1:
        # O maior número a ser testado é floor(sqrt(n))
        testMax = floor(sqrt(n))
        for i in range(2, testMax+1):
            if n % i == 0:
                return False
        return True
    else:
        return False


def primos_gemeos(n):
    # Gerar listas de primos
    primes = []
    twinPrimes = []
    for x in range(3, 10000):
        if isPrime(x):
            primes += [x]

    j = 0

    for i in range(len(primes) - 1):
        if j < n:
            if primes[i + 1] == primes[i] + 2:
                twinPrimes += [(primes[i], primes[i+1])]
                j += 1
    return twinPrimes

print(primosGemeos(10))
