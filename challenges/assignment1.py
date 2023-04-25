#ASSIGNING VARIABLES
fName = "Marco"
lName = "Breton"
fullName = """Marco
Breton"""
fAndlName = fName + " " + lName

#DISPLAY STRINGS
print(fAndlName)
print(fullName)

#USING len() FUNCTION AND in KEYWORD
print(len(fName))
print("Mar" in fName)

#DISPLAY ESCAPE CHARACTER
print("This is a qutation mark \" ")

#USING STRIP METHOD
rubbish = ("----____====::::IIIIiiiillll||||hehe hi!")
notRubbish = rubbish.strip("-_=:Iil|")
print(notRubbish)

#USING upper() METHOD
doggy = "duke"
doggo = doggy.upper()
print(doggo)
