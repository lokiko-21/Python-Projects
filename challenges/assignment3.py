animal = ('zebra', 'alligator', 'giraffe', 'goat', 'ox')

listOfAnimals = list(animal)
print(listOfAnimals)

listOfAnimals.append ("honey badger")
print(listOfAnimals)

myString = "Hello! I'm pleased to meet you"
newString = list(myString)
print(newString)

newString = myString.split(" ")
print(newString)

print(" ")
print(" ")

myList = [2, 3, 4]
len(myList)

myList.append(5)

for i in myList:
    print(i)

mySecondList = [6, 7, 8, 9, 10, 11]
myNewList = myList + mySecondList
myFakeList = myList.copy()
print(myFakeList)

listOfAnimals.reverse()
print(listOfAnimals)

mytup = ('bacon', 'egg', 'cheese')
for i in mytup:
    print(i)
mytupCount = mytup.count('egg')
print(mytupCount)

print(" ")
print(" ")

mySet = {'shirt', 'pants', 'socks', 'hat'}
for i in mySet:
    print(i)
print(" ")
mySet.add('shoes')
mySet.remove('hat')
for i in mySet:
    print(i)
print(" ")
notMySet = {'glasses', 'watch', 'shoes', 'necklace', 'socks'}
newSet = mySet.difference(notMySet)
for i in newSet:
    print(i)

print(' ')
print(' ')
print(' ')

#USING A DICTIONARY WITH KVP's
myDictionary = {'index': 1, 'index2': 2, 'index3': 355}
dic_users = {'em_1234': {'fname': 'bob', 'lname': 'smith', 'phone': '123-456-7890'},
             'em_1235': {'fname': 'mary', 'lname': 'poppins', 'phone': '321-654-0987'} }
print(dic_users)
#DISPLAYING DICTIONARY IN AN EASIER WAY TO READ FOR THE USER
print('user: {} {}\nPhone: {}'.format(dic_users['em_1235']['fname'], dic_users['em_1235']['lname'], dic_users['em_1235']['phone']) )



