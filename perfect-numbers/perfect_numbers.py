def divisor_generator(number):
    for i in xrange(1,number/2):
        if number%i == 0:
            b = number/i
            yield i,b


def is_perfect(number):
    aliquot_sum = 0
    for (a,b) in divisor_generator(number):
        if a > b:
            break
        aliquot_sum += a
        if not a == 1:
            aliquot_sum += b
    if aliquot_sum == number:
        return True
    else:
        return False

if __name__ == "__main__":
    print list(divisor_generator(28))
