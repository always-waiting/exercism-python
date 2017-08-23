class BufferFullException(Exception):
    pass


class BufferEmptyException(Exception):
    pass

class CircularBuffer(object):
    def __init__(self, size):
        bufferstr = "[],"*size
        exec("self.buffer = %s"%bufferstr)
        self.buffer_readidx = size/2
        self.buffer_writeidx = size/2
        self.size = size
        self.buffer_item = 0

    def read(self):
        if self.buffer_item == 0:
            raise BufferEmptyException
        self.buffer_item -= 1
        ret = self.buffer[self.buffer_readidx].pop()
        self.buffer_readidx = (self.buffer_readidx + 1)%self.size
        return ret

    def write(self,value):
        if self.buffer_item == self.size:
            raise BufferFullException
        self.buffer_item += 1
        self.buffer[self.buffer_writeidx].append(value)
        self.buffer_writeidx = (self.buffer_writeidx + 1)%self.size

    def clear(self):
        map(lambda x: x.pop(), self.buffer)
        self.buffer_readidx = self.size/2
        self.buffer_writeidx = self.size/2
        self.buffer_item = 0

    def overwrite(self, value):
        try:
            self.buffer[self.buffer_writeidx].pop()
        except IndexError,e:
            self.buffer_item += 1
        self.buffer[self.buffer_writeidx].append(value)
        self.buffer_writeidx = (self.buffer_writeidx + 1)%self.size
        self.buffer_readidx = (self.buffer_readidx + 1)%self.size

if __name__ == "__main__":
    obj = CircularBuffer(2)
    print obj.buffer
