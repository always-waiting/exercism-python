# -*- encoding: UTF8 -*-
def primitive_triplets(number, minnum = None, maxnum=""):
    """
    number is even
    """
    if number&1 == 1:
        raise ValueError
    ret = set()
    if number < 3:
        return ret
    number2 = number**2
    num = number>>1
    num1 = num*num - 1
    num2 = num*num + 1
    if is_add(float(num1),float(num2), minnum, maxnum):
        if number > 5:
            ret.add((number, num1, num2))
        else:
            ret.add((num1, number, num2))
    maxnumber = min(num2,maxnum)
    minnumber = max(3, minnum)
    for a in range(minnumber,maxnumber,2):
        a2 = a**2
        c2 = a2 + number2
        c = c2**0.5
        if is_add(c,a):
            if a<number:
                ret.add((a, number, int(c)))
            else:
                ret.add((number, a, int(c)))
        if a2<number2:
            c2 = number2 - a2
            c = c2**0.5
            if is_add(c,a):
                if c < a:
                    ret.add((c, a, number))
                else:
                    ret.add((a,c,number))
        else:
            c2 = a2 - number2
            c = c2**0.5
            if is_add(c,a):
                if c < number:
                    ret.add((c, number, a))
                else:
                    ret.add((number, c, a))
    return ret

def is_add(a,b, minnum = None, maxnum = ""):
    if not a > 0:
        return False
    if not b > 0:
        return False
    if not (a > minnum and a < maxnum):
        return False
    if not (b > minnum and b < maxnum):
        return False
    if a.is_integer():
        if is_prime(a,b):
            return True
    return False

def is_prime(a,b):
    if (mgcd(a,b) == 1):
        return True
    else:
        return False

def mgcd(a,b):
    if a < b:
        t = a
        a = b
        b = t
    while(a%b):
        t = b
        b = a%b
        a = t
    return b

def triplets_in_range(minnum, maxnum):
    ret = set()
    for number in range(1, maxnum):
        if number&1 == 0:
            primeset = primitive_triplets(number, 1, maxnum)
            for (a,b,c) in primeset:
                if a >= minnum and c <= maxnum:
                    ret.add((a,b,c))
                for i in range(2,maxnum/2):
                    if c*i <= maxnum and a*i >= minnum:
                        ret.add((a*i,b*i,c*i))
    return ret


def is_triplet(g):
    sm = sorted(list(g))
    if sm[0]**2 + sm[1]**2 == sm[2]**2:
        return True
    else:
        return False
