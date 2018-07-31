#imports the ability to get a random number (we will learn more about this later!)
from random import *

#Create the list of words you want to choose from.
ListSides = ["Bread", "Guacamole", "Potatoes", "Fruit", "Rice"]
ListMains = ["Chicken", "Pasta", "Soup", "Pizza", "Salmon"]
ListDesserts = ["Pudding", "Cookie", "Ice Cream"]

#Generates a random integer.

response = input("Would you like dinner?(Y/N?)")
while response != "N":
    if response == "Y":
        aRandomIndex = randint(0, len(ListSides)-1)
        print(ListSides[aRandomIndex])
        aRandomIndex = randint(0, len(ListMains)-1)
        print(ListMains[aRandomIndex])
    else:
        print("{} is an invalid input.".format(response))
    response = input("Would you like dinner? (Y/N?)")
