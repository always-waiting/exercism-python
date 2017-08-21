import re
def is_isogram(string):
    astring = re.sub("\W","",string).lower()
    b = set(astring)
    if len(b) == len(astring):
        return True
    else:
        return False
