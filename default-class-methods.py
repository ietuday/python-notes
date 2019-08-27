# When writing a class, you can override these methods to do whatever you want:
def __init__(self, x, y):
    self.x, self.y = x, y
    def __repr__(self):
    return "Represent(x={1},y=\"{2}\")".format(self.x, self.y)
    def __str__(self):
    return "Representing x as {1} and y as {2}".format(self.x, self.y)

r = Represent(1, "Hopper")
