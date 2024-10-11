class Rectangle:
    def __init__(self, length, breadth):
        self.length=length
        self.breadth= breadth

    def __iter__(self):
        yield f"length: {self.length}"
        yield f"breadth: {self.breadth}"

rec= Rectangle(12,18)
for side in rec:
    print(side)
