import math
class Circle:
    radius: int = 1
    
    def __init__(self, rad) -> None:
        self.radius = rad
        
    def calculate_area(self) -> float:
        return math.pi * self.radius**2
    
    def calculate_perimeter(self) -> float:
        return 2 * math.pi * self.radius
    
    def __str__(self) -> str:
        return f"Circle R={self.radius}, S={self.calculate_area()}, P={self.calculate_perimeter()}"

class Rectangle:
    width: int = 1
    height: int = 1
    
    def __init__(self, w, h) -> None:
        self.width = w
        self.height = h
        
    def calculate_area(self) -> float:
        return self.width * self.height
    
    def calculate_perimeter(self) -> float:
        return 2 * (self.width + self.height)
    
    def __str__(self) -> str:
        return f"Rectangle W={self.width}, H={self.height}, S={self.calculate_area()}, P={self.calculate_perimeter()}"
# Demo
if __name__ == "__main__":
    # C1 = Circle(5)
    # C2 = Circle(9)
    # print(C1)
    # print(C2)
    
    shapes = []
    shapes.append(Circle(71))
    shapes.append(Circle(19))
    
    for shape in shapes:
        print(shape)
    