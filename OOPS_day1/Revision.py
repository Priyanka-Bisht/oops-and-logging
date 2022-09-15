# First set

class Person1:
    def __init__(self, name, email, age, salary, location):
        self.name = name
        self.email = email
        self.age = age
        self.salary = salary
        self.location = location

pri = Person1("priya", "pri@gmail.com", 34,7, "delhi")
vinn = Person1("vinn","vin@gmail.com",89,110,"gadhera")
print(vinn.location)
print(pri.salary)


# Second set

class Operation:
    def __init__(self,name,yob,qualification,location):
        self.name = name
        self.yob = yob
        self.qualification = qualification
        self.location = location

    def current_age(self,current_year):
        return current_year - self.yob

pink = Operation("pink",1999,"graduate","almora")
vinny = Operation("vinny",1997,"graduate","delhi")
print(pink.current_age(2022))
print(vinny.current_age(2022))
print(vinny.qualification)
print(pink.yob)



# Third set

class Person:
    def __init__(self,name,surname,email,yob):
        self.name = name
        self.surname = surname
        self.email = email
        self.yob = yob

    def __init__(self,name,surname):
        self.name = name
        self.surname = surname

    def age(self,current_year):
        return current_year

# priyanka = Person("priyanka","bisht","priyanka@gmail.com",1998)
# vivek = Person("vivek","balodi","vivek@gmail.com",1996)

priyanka = Person("priyanka","bisht")
vivek = Person("vivek","balodi")

print(vivek.age(2022))
print(priyanka.age(2022))
print(priyanka.name)


# Fourth set

class Introduction:
    def age(self,current_year,yob):
        return current_year - yob

    def email(self,email):
        print("This is mail id of user:",email)

    def ask_name(self):
        name = input("Please enter your name: ")
        return name

    def ask_dob(self):
        dob = int(input("Please enter your dob: "))
        return dob

avni= Introduction()
kashika = Introduction()

# print(avni.ask_name())
print(avni.age(2022,2016))
print(himansh.ask_name())  # it is not going to print himansh name bcz we have not defined himansh variable above.
print(kashika.email("kashika@gmail.com"))



