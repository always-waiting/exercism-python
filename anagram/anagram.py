def detect_anagrams(string, candid):
    ret = []
    string_n = string[0].lower() + string[1:]
    strset = set(string_n)
    strlist = sorted(list(string_n))
    for stritem in candid:
        stritem_n = stritem[0].lower()+ stritem[1:]
        stritemlist = sorted(list(stritem_n))
        if set(stritem_n) != strset:
            continue
        elif stritemlist != strlist:
            continue
        elif stritem_n == string_n:
            continue
        else:
            ret.append(stritem)
    return ret

