class Luhn(object):
    def __init__(self, number_str):
        self.strnum = number_str.replace(" ","")

    def is_valid(self):
        if not self.strnum.isdigit():
            return False
        if len(self.strnum) < 2:
            return False
        sum = 0
        for item in self.strnum[-2::-2]:
            num = 2*(int(item))
            sum += num - 9 if num > 9 else num
        for item in self.strnum[-1::-2]:
            sum += int(item)
        if sum % 10 ==0:
            return True
        else:
            return False




