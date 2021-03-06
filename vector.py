class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, vector):
        return Vector(self.x + vector.x, self.y + vector.y)

    def subtract(self, vector):
        return Vector(self.x - vector.x, self.y - vector.y)

    def scalar_mult(self, vector):
        return self.x * vector.x + self.y * vector.y

    def __eq__(self, other):
        return self.x == other.x and self.y == self.y
