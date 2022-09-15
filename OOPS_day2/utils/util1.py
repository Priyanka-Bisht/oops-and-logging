class Person2:
    def __init__(self,name,surname,yob):
        self._name1 = name
        self.__surname1 = surname
        self.yob = yob

pink = Person2("priyanka","bisht",1999)
print(pink._name1)
print(pink._Person2__surname1)