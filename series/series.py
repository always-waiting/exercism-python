def slices(string, num):
    ret = []
    if num == 0:
        raise ValueError
    if len(string) < num:
        raise ValueError
    for i in range(0,len(string)-num+1):
        ret.append(map(int, string[i:i+num]))
    return ret
