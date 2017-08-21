def rotate(plain, num):
    ret = []
    for i in plain:
        if i.isalpha():
            new_str = rotate_with_num(i, num)
            ret.append(new_str)
        else:
            ret.append(i)
    return "".join(ret)

def rotate_with_num(a, num):
    ascii_code = ord(a)
    ascii_code_new = ascii_code + num
    if a.islower(): # 97~122
        if ascii_code_new > 122:
            ascii_code_new -= 26
    else: # 65~90
        if ascii_code_new > 90:
            ascii_code_new -= 26
    return chr(ascii_code_new)

