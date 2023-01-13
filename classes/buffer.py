
class BufferFile:
    def __init__(self, parent, max_size, name):
       NotImplementedError

    def __delete__(self, instance):
        NotImplementedError

    def changeOrder(self, location):
       NotImplementedError
    
    def push(self, elem):
       NotImplementedError

    def consume(self):
        NotImplementedError