myDictionary = {'triangle': 3, 'square': 4, 'hexagon': 6, 'octagon': 8}

family = {'human': {'marco': 20, 'kevin': 32, 'max': 44},
          'dog': {'duke': 2, 'lucci': 1}}
a = myDictionary.get('square')
print(a)
myDictionary['square'] = '4-sides'
a = myDictionary.get('square')
print(a)
myDictionary['pentagon'] = 5
print(myDictionary)

x = ('key1', 'key2', 'key3')
y = 3
newDictionary = dict.fromkeys(x, y)
print(newDictionary)
