#CREATING 2 CHILD CLASSES FROM A PARENT CLASS
#EACH CHILD CLASS SHOULD HAVE 2 UNIQUE ATTRIBUTES

#CREATING PARENT CLASS
class Animal:
    color = ""
    numberOfLegs = 0
    habitat = ""
    food = ""

#CREATING CHILD CLASS 1
class Dog(Animal):
    breed = ""
    humanPreference = ""

#CREATING CHILD CLASS 2
class Whale(Animal):
    species = ""
    sizeRank = ""
