import math 

#%%
class Cylinder:
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height
    def surface_area(self):
        sa = 2 * math.pi * self.radius (self.radius + self.height)
        self.sa = sa
        return sa 

    def volume(self):
        vol = math.pi * (self.radius ** 2) * self.height
        self.volume = vol
        return vol
    def __repr__(self):
        return f'The Cylinders raidius is: {self.radius} and its height is: {self.height}'

    def __add__(self,cylinder):
        new_rad = self.radius + cylinder.radius
        new_height = self.height + cylinder.height
        return Cylinder(new_rad, new_height)


my_cylinder = Cylinder(5, 2)
cylinder_2 = Cylinder(4,3)

new_cylinder = cylinder_2 + my_cylinder

#%%
class Shape:
    def __init__(self, num_sides):
        self.sides = num_sides

class Rectangle:
    def __init__(self, width, length):
        self.width = width
        self.length = length 

    def area(self):
        return self.width * self.length

class Square(Rectangle):
    def __init__(self, length_of_side):
        super().__init__(length_of_side, length_of_side)

square = Square(10)

print(square.area())
# %%
