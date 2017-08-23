from string import ascii_uppercase, digits
from random import choice

class Robot(object):
    used_names = []

    def __init__(self):
        self.reset()

    def __getattribute__(self, attr):
        if attr == 'name':
            if self._name is None:
                self.generate_name()
            return self._name
        else:
            return super(Robot, self).__getattribute__(attr)

    def generate_name(self):
        name = None
        while name in self.used_names:
            name = ''.join((choice(ascii_uppercase),
                            choice(ascii_uppercase),
                            choice(digits),
                            choice(digits),
                            choice(digits)))
        self.used_names.append(name)
        self._name = name

    def reset(self):
        self._name = None
