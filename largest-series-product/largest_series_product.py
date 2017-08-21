def largest_product(string, number):
    if number == 0: return 1
    if len(string) < number: raise ValueError
    if not string.isdigit(): raise ValueError
    if number < 0: raise ValueError
    nrange = range(0,len(string) - number +1)
    product_max = 0;
    for i in nrange:
        substr = string[i:i+number]
        sum1 = 0
        product1 = 1
        for j in substr:
            product1 *= int(j)
        if product1 > product_max:
            product_max = product1
    return product_max
