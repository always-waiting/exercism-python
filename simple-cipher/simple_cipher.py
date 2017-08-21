import re
import time
import random
random.seed(int(time.time()))
length = 100
keyinit = "".join([chr(random.randint(97,122)) for i in range(0,100)])

class Cipher(object):
    def __init__(self, key=keyinit):
        if not key.isalpha():
            raise ValueError
        if not key.islower():
            raise ValueError
        numkey = []
        for item in key:
            numkey.append(ord(item)-97)
        self.caesar = Caesar(numkey)
        self.key = key
    def encode(self, strs):
        return self.caesar.encode(strs)

    def decode(self, strs):
        return self.caesar.decode(strs)

class Caesar(object):
    def __init__(self, jump=[3]):
        self.jump = jump

    def encode(self, strs):
        plain_code = re.sub("[^a-z]","",strs.lower())
        ret=[]
        for idx, item in enumerate(plain_code):
            jump_idx = idx%len(self.jump)
            ascii = ord(item)+self.jump[jump_idx]
            if ascii > 122:
                ascii -= 26
            ret.append(chr(ascii))
        return "".join(ret)

    def decode(self, strs):
        ret = []
        for idx,item in enumerate(strs):
            jump_idx = idx%len(self.jump)
            ascii = ord(item)-self.jump[jump_idx]
            if ascii < 97:
                ascii += 26
            ret.append(chr(ascii))
        return "".join(ret)
