import re
def is_pangram(string):
    astring = re.sub("\W","",string).lower()
    b = set(astring)
    sum = 0;
    for i in b:
        if i.isalpha():
            sum += ord(i)
    if sum == 2847:
        return True
    else:
        return False
