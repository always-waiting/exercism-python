import re
def encode(strs):
    plain = re.sub("\W","", strs).lower()
    length = len(plain)
    r_ = length**0.5
    c = int(r_) if r_.is_integer() else int(r_+1)
    r = int(r_)
    pwd = []
    for i in range(0,c):
        tmp = []
        for j in range(0,r):
            try:
                tmp.append(plain[c*j+i])
            except:
                pass
        pwd.append("".join(tmp))


    return " ".join(pwd)

if __name__ == "__main__":
    print encode("If man was meant to stay on the ground, god would have given us roots.")


