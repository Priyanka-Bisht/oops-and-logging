import OOPS1
print(OOPS1)
obj3 = OOPS1.Person("priyanka","bisht",1997)
print(obj3.yob)
print(obj3._name1)
print(obj3._Person__surname1)

class Person:
    _name = "pink"
    __surname = "bisht"
    yob = 1999

    def _age(self,current_year):
        return current_year - self.yob

    def __age(self,current_year):
        return current_year - self.yob

obj = Person()
print(obj._age(2022))
print(obj._Person__age(2022))

class employee(Person):
    _name = "priyanka"
    __surname = "balodi"
    yob = 1998

obj1 = employee()
print(obj._age(2022))
print(obj1._Person__age(2022))

print(obj1)
print(obj1.yob)
print(obj1._name)
print(obj1._Person__surname)
print(obj1._employee__surname)

