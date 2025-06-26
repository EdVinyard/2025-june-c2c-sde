import math

class Rectangle:
    def __init__(self, length_mm, width_mm):
        self.length_mm = length_mm
        self.width_mm  = width_mm

    def area_sq_mm(self):
        return self.length_mm * self.width_mm


longer = Rectangle(6.0, 1.0)
print(longer.area_sq_mm())            #  6.0
wider = Rectangle(2.0, 5.0)
print(wider.area_sq_mm())             # 10.0
square = Rectangle(3.0, 3.0)
print(square.area_sq_mm())            #  9.0
