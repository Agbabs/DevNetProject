#Write a Python program that calculates the area of a circle 
#based on the radius entered by the user.

import math
radius = float(input("Enter the radius of the circle : " ))
area = math.pi*radius*radius
print("area of a circle is :" , area)