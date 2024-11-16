#Write a Python program to display the first and last colors from the following list.
#color_list = ["Red","Green","White" ,"Black"]

colour = ["Red", "Green", "White", "Black"]

print(colour)

print(colour[0], colour[3])

#Anotherway is to use 
# #import itemgetter.

colour = ["Red", "Green", "White", "Black"]
from operator import itemgetter
print(itemgetter(1, 2)(colour))
