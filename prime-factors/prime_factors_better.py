def prime_factors(strs):
    result = []
    float=2
    while float:
        if strs%float==0:
            strs = strs / float
            result.append(float)
        else:
            float = float+1
            if float>strs:
                break
    return result
