class Kwadrat:

    def __init__(self, x):
        self.x = x
        self.y = x

    def __add__(self,z):
        return self.x+z.x, self.y+z.x
k1 = Kwadrat(3)
k2= Kwadrat(8)
k3=k1+k2
print(k3)