class BinaryFile:
    def __init__(self, parent, name, info):
        if (parent.count_elems >= parent.DIR_MAX_ELEMS ):
            print('Parent directory is full.')
            return
        self.parent = parent
        self.parent.count_elems += 1
        self.name = name
        self.info = info
        self.parent.list.append(self)

    def __delete__(self, instance):
       print('Directory has deleted.')
       return

    def changeOrder(self, location):
       if (location.count_elems >= location.DIR_MAX_ELEMS):
            print('Directory is full. Can\'t changeOrder.')
            return
       self.parent.count_elems -=1 
       index = self.parent.list.index(self)
       self.parent.list.pop(index)
       self.parent = location
       self.parent.list.append(self)
       self.parent.count_elems +=1 
    
    def get(self):
        return self.info