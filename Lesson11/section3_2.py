class Rectangle:
    def __init__(self, length_mm, width_mm):
        self.length_mm = length_mm
        self.width_mm = width_mm

    def area_sq_mm(self):
        return self.length_mm * self.width_mm

class Square(Rectangle):
    def __init__(self, side_mm):
        super().__init__(side_mm, side_mm)


longer = Rectangle(60.0, 10.0)
print(longer.area_sq_mm())            # 600.0
wider = Rectangle(20.0, 50.0)
print(wider.area_sq_mm())             # 1000.0
square = Square(30.0)
print(square.area_sq_mm())            # 900.0
