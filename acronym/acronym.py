import re
def abbreviate(string):
    slist = re.split("\W",string)
    ret = []
    for i in slist:
        if len(i) > 0:
            ret.append(i[0].upper())
    return "".join(ret)

