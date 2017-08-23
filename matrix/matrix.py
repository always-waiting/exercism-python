class Matrix(object):
    def __init__(self, numstrs):
        number_lines = numstrs.split("\n")
        self._data = []
        for line in number_lines:
            self._data.append(map(lambda x:int(x),line.split(" ")))

    @property
    def rows(self):
        return self._data

    @property
    def columns(self):
        return [map(lambda x: x[i],self._data) for i in range(0,len(self._data[0]))]

