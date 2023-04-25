mySentence = 'loves the color'
colorList = ['red', 'blue', 'green', 'pink', 'teal', 'black']

def colorFunction(name):
    lst = []
    for i in colorList:
        msg = "{0} {1} {2}".format(name, mySentence, i)
        lst.append(msg)
    return lst

def getName():
    go = True
    while go:
        name = input('What is your name? ')
        if name == '':
            print('You need to provide your name.')
        elif name == 'Max':
            print('Max you can\'t use this software, sorry not sorry -_-')
        else:
            go = False
    lst = colorFunction(name)
    for i in lst:
        print(i)



getName()
