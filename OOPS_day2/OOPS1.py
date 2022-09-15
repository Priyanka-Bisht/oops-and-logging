
from utils.util1 import Person2
obj = Person2("priyanka","bisht",1999)
print(obj.yob)


class Person:
    def __init__(self,name,surname,yob):
        self._name1 = name
        self.__surname1 = surname
        self.yob = yob

pink = Person("priyanka","bisht",1999)
print(pink._name1)
print(pink._Person__surname1)