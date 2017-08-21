from math import sqrt


def prime_factors(n):
    primes = sieve(int(sqrt(n)) + 1)
    n_factors = []
    for p in primes:
        while n % p == 0:
            n_factors.append(p)
            n = n // p
    if n != 1:
        return n_factors + [n]
    else:
        return n_factors


def sieve(n):
    '''Sieve of Eratosthenes'''
    rng = list(range(3, n + 1, 2))

    # Sieve out anything divisible by the first element of rng
    def _sieve(rng):
        p = rng[0]
        return [i for i in rng if i % p]

    ret = []
    while rng:
        ret, rng = ret + [rng[0]], _sieve(rng)
    return [2] + ret

