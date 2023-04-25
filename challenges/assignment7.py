num1 = 12
key = False

if num1 == 12:
    if key:
        print('num1 is 12 and they have the key!')
    else:
        print('num1 is 12 but they don\'t have the key')
elif num1 < 12:
    print('num1 is less than 12')
else:
    print('num1 is not 12')

#USING BOOL FUNCTION
a = bool(21)
print(a)

#USING ISINSTANCE FUNCTION
b = isinstance(num1, str)
print(b)

i = 1

while i < 11:
    print('this loop has gone through {} time(s)'.format(i))
    i += 1
    if i < 7:
        print('_____________________')
        continue
    else:
        break

myList = ['red', 'green', 'blue', 'yellow', 'orange', 'purple', 'pink']

for i in myList:
    if i == 'orange':
        continue
    elif i == 'purple':
        break
    print(i)
