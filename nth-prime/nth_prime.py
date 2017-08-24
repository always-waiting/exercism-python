def nth_prime(number):
    if number <= 0:
        raise ValueError
    loop = 1
    detected_number = 2
    product = 1
    num = 1
    if num == number:
        return detected_number
    while num != number:
        detected_number = 2*loop+1
        if gcd(product, detected_number) == 1:
            product *= detected_number
            num += 1
        loop += 1
    return detected_number

def gcd(a,b):
    if a < b:
        t=a
        a=b
        b=t
    while(a%b):
        m = a % b
        a = b
        b = m
    return b

