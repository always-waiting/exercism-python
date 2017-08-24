def divisor_generator(n):
    for i in range(1, int(n**.5)+1):
        if n % i == 0:
            yield i
            yield n//i

def is_perfect(n):
    return sum(divisor_generator(n)) == 2*n
