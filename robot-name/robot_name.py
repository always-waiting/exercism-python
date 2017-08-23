import random

class Robot(object):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWYZ"
    def __init__(self, loop = 1):
        s1=""
        s2=""
        nums=0
        for i in range(0,loop):
            s1 = random.choice(Robot.alpha)
            s2 = random.choice(Robot.alpha)
            nums = random.randint(100,999)
        self.name = "%s%s%d"%(s1,s2,nums)
        self.loop = loop

    def reset(self):
        self.loop += 1
        self.__init__(self.loop)
