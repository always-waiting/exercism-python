def encode(string):
    ret = []
    for i in string.lower():
        if i.isalpha():
            if len(ret) == 0:
                ret.append(chr(219-ord(i)))
            elif len(ret) % 5 == 0:
                ret.append(" "+chr(219-ord(i)))
            else:
                ret.append(chr(219-ord(i)))
        elif i.isdigit():
            if len(ret) == 0:
                ret.append(i)
            elif len(ret) % 5 == 0:
                ret.append(" "+i)
            else:
                ret.append(i)

    return "".join(ret)


def decode(string):
    ret = []
    for i in string:
        if i.isalpha():
            ret.append(chr(219-ord(i)))
        elif i.isdigit():
            ret.append(i)
    return "".join(ret)
