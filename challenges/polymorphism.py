#parent class
class Animal:
    species = "Unknown"
    arms = 0
    legs = 0

    def habitat(self):
        entry_habitat = input("Does this animal live on land or underwater?")
        if (entry_habitat == "land"):
            print("is a land animal")
        elif (entry_habitat == "underwater"):
            print("is an underwater animal")
        else:
            print("Please write 'land' or 'sea'.")

#child class 1
class Dog(Animal):
    breed = "Pomeranian"
    fur_color = "White"

    def habitat(self):
        entry_habitat = input("should Pomeranians be outside or inside?")
        if (entry_habitat == "outside"):
            print("Pomeranian breeds shuold stay outside.")
        elif (entry_habitat == "inside"):
            print("Pomeranian breeds shuold stay inside.")
        else:
            print("Please type 'inside' or 'outside'.")

#child class 2
class Bird(Animal):
    breed = "Penguin"
    feather_color = "black & white"
    can_fly = False

    def habitat(self):
        entry_habitat = input("Should Penguins live in a zoo or in the wild?")
        if (entry_habitat == "zoo"):
            print("Penguins should live in a zoo!")
        elif (entry_habitat == "wild"):
            print("Penguins deserve to be free!")
        else:
            print("Please write 'zoo' or 'wild'.")

dog = Dog()
dog.habitat()

bird = Bird()
bird.habitat()

animal = Animal()
animal.habitat()









            
