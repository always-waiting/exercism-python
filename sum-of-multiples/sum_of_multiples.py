def sum_of_multiples(total, candid):
    totallist = range(1,total)
    ret = []
    for i in totallist:
        insert = False
        for j in candid:
            if i%j == 0:
                insert = True
                break
        if insert: ret.append(i)
    return sum(ret)
