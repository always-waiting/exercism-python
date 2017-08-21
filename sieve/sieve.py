def sieve(total):
    totallist = range(1,total+1)
    ret  = []
    if len(totallist) == 1:
        return ret
    for num in totallist[1:]:
        if num in [2,3,5,7,11,13]:
            ret.append(num)
        else:
            insert = True
            for prime in ret:
                if num % prime == 0:
                    insert = False
                    break
            if insert: ret.append(num)

    return ret
