class parzy:
    """Iterator zwracający wartości w odwróconym porządku"""
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 2
        return self.data[self.index]
a=parzy("Hej")
#print(a.__next__())
b=parzy("Czesc")
print(b.__next__())
print(b.__next__())