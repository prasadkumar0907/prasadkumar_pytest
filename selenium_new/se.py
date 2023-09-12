class Point:
    def __init__(self,a, b):
        self.a = a
        self.b = b
        self.health = 100

    def move(self,dx, dy):
        self.a += dx
        self.b += dy

    def attack(self, pts):
        self.health -= pts


Point.health = 99

#
# p1 = Point(1, 2)
# print(p1.__dict__)
# print(p1.move(3,4))
# print(p1.__dict__)
# print(p1.attack(9))
# print(p1.__dict__)
# print(p1.__class__.__dict__)
