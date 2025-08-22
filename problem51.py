class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        result = Vector(self.x + other.x, self.y + other.y, self.z + other.z)
        return result 
    
    def __mul__(self, other):
        # Dot product returns a scalar, not a Vector
        return self.x * other.x + self.y * other.y + self.z * other.z

    def __str__(self):
        #return f"vector({self.x}, {self.y}, {self.z})"
        return f"{self.x}i + {self.y}j + {self.z}k"
    
v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)
v3 = Vector(7, 8, 9)
print(v1 + v2)
print(v1 * v2)

print(v2 + v3)
print(v1 * v3)
