# -*- encoding: UTF8 -*-
import sys
# will be failed when input 490 ~ 499!!
# should improve!!
a2n = {
    1    : "I",
    5    : "V",
    10   : "X",
    50   : "L",
    100  : "C",
    500  : "D",
    1000 : "M"
}
def numeral(arabic):
    ret = []
    baselist = sorted(a2n.keys(),reverse=True)
    for idx,base in enumerate(baselist):
        num = arabic/base
        if num == 0:
            try:
                base1 = baselist[idx + 2]
            except:
                continue
            if base1 in [1, 10, 100]:
                arabic1 = arabic + base1
                num1 = arabic1/base
                if num1 == 1:
                    ret.append(a2n[base1]+a2n[base])
                    arabic = arabic + base1 - base
        elif num == 4:
            ret.append(a2n[base] + a2n[baselist[idx-1]])
            arabic = arabic + base - baselist[idx-1]
        else:
            ret.append(a2n[base]*num)
            arabic = arabic - base*num
    return "".join(ret)


if __name__ == "__main__":
    print numeral(int(sys.argv[1]))
