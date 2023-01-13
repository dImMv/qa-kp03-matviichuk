from itertools import count


class BufferFile:
    def __init__(self, parent, max_size, name):
       if (parent.count_elems >= parent.DIR_MAX_ELEMS ):
            print('Parent directore is full')
            return
       self.parent = parent
       self.parent.count_elems += 1
       self.parent.list.append(self)
       self.MAX_BUF_FILE_SIZE = max_size
       self.name = name
       self.info = []

    def __delete__(self, instance):
        print("Buffer were deleted")
        return

    def changeOrder(self, location):
       if (location.count_elems >= location.DIR_MAX_ELEMS):
            return
       self.parent.count_elems -=1
       index = self.parent.list.index(self)
       self.parent.list.pop(index)
       self.parent = location
       self.parent.list.append(self)
       self.parent.count_elems +=1

    def push(self, elem):
       if count(list) >= self.MAX_BUF_FILE_SIZE:
            print('File is full. Can\'t push new line.')
            return
       self.info.append(elem)
       

    def consume(self):
        self.info.pop()