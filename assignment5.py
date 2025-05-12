import math

class ShapeCalculator:
    def area(self, dim1, dim2=None):
        if dim2 is None:
            
            return math.pi * dim1 ** 2
        else:
            
            return dim1 * dim2


calc = ShapeCalculator()

circle_area = calc.area(5)             
rectangle_area = calc.area(4, 6)       

print(f"Area of Circle: {circle_area:.2f}")
print(f"Area of Rectangle: {rectangle_area}")