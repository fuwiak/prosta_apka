# class A:
#     def __init__(self, x, y):
#         self.x=x
#         self.y=y




# a = A(1,2)
# b = A(3,4)







class Vector2D:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Vector2D({self.x}, {self.y})"

    def __add__(self, other):
        if isinstance(other, Vector2D): # po dodaniu dwoch wektorow chce vector a nie np tuple
            return Vector2D(self.x + other.x, self.y + other.y)
        return NotImplemented
    #
    def __sub__(self, other):
        if isinstance(other, Vector2D):
            return Vector2D(self.x - other.x, self.y - other.y)
        return NotImplemented

    def __mul__(self, scalar):
        if isinstance(scalar, (int, float)):
            return Vector2D(self.x * scalar, self.y * scalar)
        return NotImplemented

    def __truediv__(self, scalar):
        if isinstance(scalar, (int, float)) and scalar != 0:
            return Vector2D(self.x / scalar, self.y / scalar)
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Vector2D):
            return self.x == other.x and self.y == other.y
        return NotImplemented

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        if isinstance(other, Vector2D):
            return self.magnitude() < other.magnitude()
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, Vector2D):
            return self.magnitude() <= other.magnitude()
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Vector2D):
            return self.magnitude() > other.magnitude()
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Vector2D):
            return self.magnitude() >= other.magnitude()
        return NotImplemented

    def __neg__(self):
        return Vector2D(-self.x, -self.y)

    def __pos__(self):
        return Vector2D(+self.x, +self.y)

    def magnitude(self):
        return (self.x**2 + self.y**2) ** 0.5

    def normalize(self):
        mag = self.magnitude()
        if mag == 0:
            return Vector2D(0, 0)
        return Vector2D(self.x / mag, self.y / mag)

# Example usage
v1 = Vector2D(3, 4)
v2 = Vector2D(1, 2)

print("Vector 1:", v1)
print("Vector 2:", v2)

# Addition
print("Addition:", v1 + v2)

# Subtraction
print("Subtraction:", v1 - v2)

# Scalar multiplication
print("Scalar Multiplication:", v1 * 2)

# Scalar division
print("Scalar Division:", v1 / 2)

# Equality
print("Equality:", v1 == v2)

# Magnitude
print("Magnitude of v1:", v1.magnitude())

# Normalization
print("Normalized v1:", v1.normalize())
