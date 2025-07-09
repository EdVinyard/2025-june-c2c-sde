# Find the following terms in the code (by line number).
#
# 1. class definition
# 2. initializer (AKA constructor)
# 3. attribute (AKA field)
# 4. method definition
# 5. method call (AKA method invocation)
# 6. object creation (AKA instantiation)

class Square: # class definition
    def __init__(self, side_mm): # initializer
        self.side_mm = side_mm # attribute

    def area_sq_mm(self): # method definition
        return self.side_mm * self.side_mm

postage_stamp = Square(31.12) # object creation
area = postage_stamp.area_sq_mm() # method call
print(str(area) + ' mm²')
