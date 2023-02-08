"""
class GP:
    def getString(self):
        self.word = input()
        
    def printString(self):
        print("Ur word in uppercase: " + str(self.word.upper()))
        
my_word = GP()
my_word.getString()
my_word.printString()

"""
"""
class Shape:
    def __init__(self, areaa):
        self.areaa = areaa

    def area(self):
        print("Area: ", self.areaa)

class Square(Shape):
    def __init__(self, areaa, length):
        # super() method helps you to use methods of Parent class (Clothing)
        super().__init__(areaa)
        self.length = length

    def area(self):
        super().area()
        print("Length: ", self.length)


area = Square(0, 4)
area.area()
"""
"""
class Shape:
    def __init__(self, areaa):
        self.areaa = areaa

    def area(self):
        print("Area: ", self.areaa)

class Square(Shape):
    def __init__(self, areaa, length):
        # super() method helps you to use methods of Parent class (Clothing)
        super().__init__(areaa)
        self.length = length

    def area(self):
        super().area()
        print("Length: ", self.length)

class Rectangle(Shape):
    def __init__(self, areaa, length, width):
        # super() method helps you to use methods of Parent class (Clothing)
        super().__init__(areaa)
        self.length = length
        self.width = width

    def area(self):
        super().area()
        print("Area of rectangle: ", self.length*self.width)


area = Rectangle (0, 4, 5)
area.area()
"""
"""
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        return (self.x, self.y)
        
    def move(self, dx, dy):
        self.x = self.x + dx
        self.y = self.y + dy

    def dist(self, other):
        dx = self.x - other.x
        dy = self.y - other.y

        return (dx**2 + dy**2)**0.5

    

point1 = Point(10,4)
point2 = Point(5,12)

print(point1.dist(point2))
point1.move(10,1)
print(point1.dist(point2))
print(point1.show())
"""
