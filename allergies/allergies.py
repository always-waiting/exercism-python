class Allergies(object):
    score2staff = {
        1   : 'eggs',
        2   : 'peanuts',
        4   : 'shellfish',
        8   : 'strawberries',
        16  : 'tomatoes',
        32  : 'chocolate',
        64  : 'pollen',
        128 : 'cats'
    }
    staff2score = {
        'eggs'          : 1,
        'peanuts'       : 2,
        'shellfish'     : 4,
        'strawberries'  : 8,
        'tomatoes'      : 16,
        'chocolate'     : 32,
        'pollen'        : 64,
        'cats'          : 128
    }
    stafflist = ['eggs','peanuts','shellfish','strawberries','tomatoes','chocolate','pollen','cats']
    def __init__(self, score):
        self.score = score
        self.bscore = bin(score)

    def is_allergic_to(self, staff):
        score = Allergies.staff2score[staff]
        bscore = bin(score)
        bscore_high = len(bscore)-2
        if len(self.bscore) < len(bscore):
            return False
        if self.bscore[-bscore_high] == '1':
            return True
        else:
            return False

    def get_lst(self):
        ret = []
        for item in Allergies.stafflist:
            if self.is_allergic_to(item):
                ret.append(item)
        return ret

    lst = property(get_lst)


