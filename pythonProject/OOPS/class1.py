class Parent:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a+self.b


class Child(Parent):
    def __init__(self, r, t, h, j):
        self.t = t
        self.r = r
        super().__init__(h, j)

    def display(self):
        print(self.r * self.t)
        print("In child class")

c1 = Child(2, 4, 7, 8)

c1.display()
print(c1.add())

