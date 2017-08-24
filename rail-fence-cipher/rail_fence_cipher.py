def fence_pattern():
    pass


def encode(plain, lines):
    ret = []
    stepsum = 2*(lines - 1)
    for line in range(lines):
        idx = line
        stepf = 2*(lines-line-1)
        if stepf ==0: stepf = stepsum - stepf
        while idx <= len(plain)-1:
            try:
                ret.append(plain[idx])
            except:
                break
            idx = idx + stepf
            if not stepf == stepsum:
                stepf = stepsum - stepf
    return "".join(ret)



def decode(code, lines):
    ret = []
    ret_idx = []
    stepsum = 2*(lines-1)
    #for idx_c in range(len(code)):
    for line in range(lines):
        idx = line
        stepf = 2*(lines-line-1)
        if stepf ==0: stepf = stepsum - stepf

        while idx <= len(code) - 1:
            ret_idx.append(idx)
            idx = idx + stepf
            if not stepf == stepsum:
                stepf = stepsum - stepf
    for idx,value in enumerate(ret_idx):
        ret.append({value:code[idx]})
    ret = sorted(ret, key=lambda x: x.keys()[0])
    ret = map(lambda x: x.values()[0],ret)
    return "".join(ret)


if __name__ == "__main__":
    print decode("ESXIEECSR",4)
