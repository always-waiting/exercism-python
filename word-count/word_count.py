import re
def word_count(word):
    count = {}
    words = filter(lambda x:x,re.split("\W|_",word.lower()))
    for name in words:
        try:
            count[name] += 1
        except KeyError:
            count[name] = 1
    return count

