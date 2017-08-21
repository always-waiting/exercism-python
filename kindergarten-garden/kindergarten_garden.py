class Garden(object):
    plants2name = {
        "G":"Grass",
        "R":"Radishes",
        "C":"Clover",
        "V":"Violets"
    }
    persons = [
        "Alice", "Bob", "Charlie", "David",\
        "Eve", "Fred", "Ginny", "Harriet",\
        "Ileana", "Joseph", "Kincaid", "Larry"\
    ]
    def __init__(self, plants, **kwargs):
        plantslist = plants.split("\n")
        self.window = plantslist[0]
        self.wall = plantslist[1]
        if len(kwargs) > 0:
            self.students = kwargs["students"]
            self.students.sort()
        else:
            self.students = Garden.persons
    def plants(self, name):
        idx = self.students.index(name)
        ret = []
        ret.extend(self.window[idx*2:idx*2+2])
        ret.extend(self.wall[idx*2:idx*2+2])
        return map(lambda x: Garden.plants2name[x], ret)
