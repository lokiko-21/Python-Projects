#CREATING PROTECTED FUNCTION/METHOD
class Encapsulate1:
    def __init__(self):
        self._protected = 6

    def getProtected(self):
        print(self._protected)

#CREATING PRIVATE FUNCTION/METHOD
class Encapsulate2:
    def __init__(self):
        self.__private = 2

    def getPrivate(self):
        print(self.__private)

    def setPrivate(self, private):
        self.__private = private

#USING PRIVATE
y = Encapsulate2()
y.getPrivate()
y.setPrivate(4)
y.getPrivate()

#USING PROTECTED
x = Encapsulate1()
print(x._protected)
x._protected = 8
print(x._protected)
