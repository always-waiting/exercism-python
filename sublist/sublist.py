EQUAL = 1
UNEQUAL = 2
SUBLIST = 3
SUPERLIST = 4
def check_lists(al,bl):
    if al == bl:
        return EQUAL
    if len(al) == 0:
        return SUBLIST
    if len(bl) == 0:
        return SUPERLIST

    atemp = map(lambda x:str(x),al)
    btemp = map(lambda x:str(x),bl)
    astr = "-".join(atemp)
    bstr = "-".join(btemp)
    a_in_b = astr in bstr
    b_in_a = bstr in astr
    if a_in_b and b_in_a:
        return EQUAL
    elif a_in_b:
        return SUBLIST
    elif b_in_a:
        return SUPERLIST
    else:
        return UNEQUAL
