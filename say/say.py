digits2eng = {
    0 : "zero",
    1 : "one",
    2 : "two",
    3 : "three",
    4 : "four",
    5 : "five",
    6 : "six",
    7 : "seven",
    8 : "eight",
    9 : "nine",
    10 : "ten",
    11 : "eleven",
    12 : "twelve",
    14 : "fourteen"
}
tens2eng = {
    1 : "teen",
    2 : "twen",
    3 : "thir",
    4 : "for",
    5 : "fif",
    6 : "six",
    7 : "seven",
    8 : "eigh",
    9 : "nine"
}
def parser_number(number):
    ret = []
    if number < 1000:
        ret.append(number)
    else:
        ret.append(number%1000)
        ret.extend(parser_number(number/1000))
    return ret

sites = ["","thousand", "million", "billion"]
def say(number):
    if number < 0 :
        raise AttributeError
    if number >= 1e12:
        raise AttributeError
    nlist = parser_number(number)
    ret = []
    if len(nlist) == 1:
        return say_0to999(nlist[0])

    for index, value in enumerate(nlist):
        str1 = say_0to999(value)
        str2 = sites[index]
        if str1 == "zero":
            pass
        else:
            if str2 == "":
                ret.append(str1)
            else:
                ret.append(" ".join([str1,str2]))
    ret.reverse()
    if len(ret) == 2 and len(nlist) > 2:
        return " and ".join(ret)
    else:
        return " ".join(ret)

def say_0to999(number):
    if number < 100:
        return say_0to99(number)
    else:
        a = number/100
        b = number%100
        if b == 0:
            ret = [digits2eng[a], "hundred"]
        else:
            ret = [digits2eng[a], "hundred", "and", say_0to99(number%100)]
        return " ".join(ret)


def say_0to99(number):
    if number in digits2eng:
        return digits2eng[number]
    else:
        tens = number/10
        digits = number%10
        if tens == 1:
            return tens2eng[digits]+tens2eng[1]
        else:
            if digits == 0:
                return tens2eng[tens] + "ty"
            else:
                return tens2eng[tens] + "ty-" + digits2eng[digits]
