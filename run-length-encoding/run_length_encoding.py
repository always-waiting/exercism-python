import re
def decode(string):
    mycode = myCode(string)
    return mycode.decode()


def encode(string):
    mycode = myCode(string)
    return mycode.encode()

class myCode(object):
    def __init__(self,string):
        self.code = string
        self.string = string
        #if re.search("\d",string): # encoded string
        #self.code = string
        #else:
        #    self.string = string
    def encode(self):
        """
        string -> code
        """
        if len(self.string) == 0:
            return ''
        else:
            code = []
            count = []
            for char in self.string:
                if len(code) == 0:
                    code.append(char)
                    count.append(1)
                else:
                    if code[-1] == char:
                        count[-1]+=1
                    else:
                        code.append(char)
                        count.append(1)
            code_stats = map(lambda x: "%d%s"%x if x[0]!=1 else x[1],zip(count,code))
            return "".join(code_stats)



    def decode(self):
        """
        code -> string
        """
        if len(self.code) == 0:
            return ""
        else:
            count = re.compile("[^\d]+").split(self.code)
            code = re.compile("\d+").split(self.code)
            if len(code) == 1:
                return code[0]
            count.pop() # remove tail ""
            code = code[1:] # remove first ""
            strlist = []
            for i in range(len(code)):
                if len(code[i]) > 1:
                    strlist.append(code[i][0]*int(count[i])+code[i][1:])
                    pass
                else:
                    strlist.append(code[i]*int(count[i]))
            return "".join(strlist)



