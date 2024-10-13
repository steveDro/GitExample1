class Circle:
    """Class representing a person"""
    Id = 0
    radius = 0
    color = ""
    display = True

    def __init__(self, id, r, c, d):
        self.Id = id
        self.radius = r
        self.color = c
        self.display = d

    def circumstance(self) -> float:
        return 3.132 * self.radius * 2


circle1 = Circle(1, 10, "Blue", True)

print(circle1.circumstance())
