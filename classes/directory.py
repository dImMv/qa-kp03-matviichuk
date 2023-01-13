class Directory:
    def __init__(self, name, max_elems, parent = None):
        NotImplementedError

    def __delete__(self, instance):
        NotImplementedError

    def list_elems(self):
        NotImplementedError

    def changeOrder(self, location):
        NotImplementedError