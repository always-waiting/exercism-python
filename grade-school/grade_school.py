class School(object):
    def __init__(self, name):
        self.name = name
        self.gradelist = {}

    def grade(self,number):
        if not self.gradelist.has_key(number):
            return set()
        else:
            ret = self.gradelist[number][:]
            ret.sort()
            return set(ret)

    def add(self, name, grade):
        if self.gradelist.has_key(grade):
            self.gradelist[grade].append(name)
        else:
            self.gradelist[grade] = [name]

    def sort(self):
        ret = []
        for key in sorted(self.gradelist.keys()):
            ret_inner = self.gradelist[key][:]
            ret_inner.sort()
            ret.append((key,tuple(ret_inner)))
        return ret

#from types import GeneratorType
#from collections import Sequence
#These are other solutions!
#should be consideration!
