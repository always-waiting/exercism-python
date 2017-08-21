# -*- encoding: UTF8 -*-
def prime_factors(number):
    ret = []
    if number < 2:
        return ret
    half_num = number>>1
    for i in xrange(2, half_num+1):
        if isprime1(i):
            if number % i ==0:
                ret.append(i)
                number1 = number/i
                ret.extend(prime_factors(number1))
                break
    if len(ret) == 0:
        ret.append(number)
    return ret

# 费马-蒙哥马利法判断素数
# 1: 有N为任意正整数，P为素数，且N不能被P整除（显然N和P互质），则有：N^P%P=N or (N^(P-1))%P=1
# 2: "蒙格马利”快速幂模算法
prime_table = [ 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41,\
                43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97  ]
def isprime1(num):
    if num < 2:
        return False
    if num in prime_table:
        return True
    for i in prime_table:
        if (1 != Montgomery(num , i-1, i)):
            return False
    return True

def Montgomery(n,p,m):
    """
    快速计算(n^p)%m
    """
    r = n % m
    k = 1
    while (p>1):
        if p&1 != 0:
            k = (k*r)%m
        r = (r*r)%m
        p>>=1
    return (r*k)%m

def Power(n,p):
    main = n
    odd = 1
    while (p>1):
        if (p%2 == 1):
            odd *= main
        main *= main
        p/=2
    return main*odd

if __name__ == "__main__":
    print prime_factors(9)
    print isprime1(4)
