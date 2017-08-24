def nth_prime(n):
    if n <= 0:
        raise ValueError
    for i, prime in enumerate(prime_gen()):
        if n == i + 1:
            return prime

def prime_gen():
    def n_gen():
        n = 2
        while True:
            yield n
            n += 1

    nonprimes = {}
    for n in n_gen():
        prime = nonprimes.pop(n, None)
        if prime is None:
            yield n
            nonprimes[n ** 2] = n
        else:
            x = prime + n
            while x in nonprimes:
                x += prime
            nonprimes[x] = prime
        print nonprimes
