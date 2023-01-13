class LogTextFile:
    def __init__(self, parent, name, info):
        NotImplementedError

    def __delete__(self, instance):
       NotImplementedError

    def changeOrder(self, location):
        NotImplementedError
    
    def get(self):
        NotImplementedError

    def append_line(self, line):
        NotImplementedError