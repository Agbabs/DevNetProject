# 6. Write a Python program to create a class representing a Circle. Include methods to calculate its area and perimeter.'

import math
class circle_compute():
    def __init__(self,my_radius):
        self.radius=my_radius
    def area_calculate(self):
        return math.pi*(self.radius**2)
    def perimeter_calculate(self):
        return 2*math.pi*self.radius
my_result = int(input("Enter the radius of circle..."))
my_instance = circle_compute(my_result)
print("The radius enter is : ")
print(my_result)
print("The Computed area of circle is ")
print(round(my_instance.area_calculate(),2))
print("The compound perimeter of circle is : ")
print(round(my_instance.perimeter_calculate(),2))
    