import re
action = ["wink","double blink","close your eyes","jump","r"]
def handshake(input):
    ret = []
    if type(input) == int:
        if input < 0:
            return ret
        strnum = bin(input)[2:]
    else:
        if re.search("[2-9]",input):
            return ret
        strnum = input
    for idx, num in enumerate(strnum[::-1]):
        if num == "1":
            if idx != 4:
                ret.append(action[idx])
            else:
                ret.reverse()
    return ret


def code(input):
    ret = []
    if not set(input).issubset(set(action)):
        return '0'
    for idx, act in enumerate(action):
        if act in input:
            ret.append("1")
        else:
            ret.append("0")
    ret.reverse()
    if len(input) >= 2 and action.index(input[0]) > action.index(input[1]):
        ret[0] = '1'
    retstr =  "".join(ret)
    return re.sub("^0+","",retstr)
