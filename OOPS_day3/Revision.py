# OOPS1
class Grandfather:
    def __init__(self,name,age,profession):
        self.name = name
        self.age = age
        self.profession = profession

    def hobby(self):
        print("Grandfathe's hobby is to do Painting.")

class Father(Grandfather):
    def son_of_grandfather(self):
        print("Father is the son of grandfather.")

grandfather = Father("Praveen",75,"Teacher")
print(grandfather.name)
print(grandfather.profession)

# OOPS2
class Highschool:
    def __init__(self,name,schoolname):
        self.name = name
        self.schoolname = schoolname

    def Primary(self):
        print("I have done primary classes from SSM")

    def Upper_primary(self):
        print("I did my upper primary from SVM")

class Intermediate(Highschool):
    def __init__(self,school_name):
        self.school_name = school_name
        super().__init__("Priyanka","GGIC")

class UG(Intermediate):
    pass

student = Intermediate("AIC")
print(student.name)
print(student.school_name)
print(student.schoolname)

student1 = UG("AIC")
print(student1.name)
print(student1.school_name)
print(student1.schoolname)


# OOPS3
class Streetfood:
    def momos(self):
        print("it is a famouse indian street food.")

    def panipuri(self):
        print("It tastes delicious.")

    def cholekulche(self):
        print("Famous in north.")

class Fivestarhotel:
    def sushi(self):
        print("don't know how it tastes.")

    def drinks(self):
        print("There are different types of drinks.")

class Restaurents:
    def dosa(self):
        print("In india there are variety of dosa.")

    def burger(self):
        print("It is famous in the whole world.")

    def sweets(self):
        print("West bengal is famous for sweets.")

class HomemadeFood(Streetfood,Fivestarhotel,Restaurents):
    pass

i = HomemadeFood()
i.drinks()
i.sweets()
i.sushi()



# OOPS4
class ineuron:
    def __init__(self,name,course):
        self.name = name
        self.course = course

    def student_details(self):
        print("Name:",self.name)
        print("Course:",self.course)

class oneneuron(ineuron):
    def student_details(self):
        print("My name is Vivek and i bought techneuron and fsds bootcamp.")

io = oneneuron("Vivek","Datascience")
io.student_details()


# OOPS5
class Car:
    __mileage = 120

    def mileage(self):
        print("mileage is:",Car.__mileage)
c = Car()
c.mileage()
print(c._Car__mileage)


# OOPS6
class Fruits:
    def Mango(self):
        print("Mango is a seasonal fruit.")

class Season:
    def Mango(self):
        print("Mango fruits grow in summer.")

def external(m):
    m.Mango()
p = Fruits()
q = Season()
external(p)
external(q)


# OOPS7
class ineuron:
    def __init__(self):
        self.student = "Data Science"

    def students(self):
        print(self.student)

i = ineuron()
i.students()
i.student = "Big Data"
i.students()

class oneneuron:
    def __init__(self):
        self.__student = "AI"

    def students(self):
        print(self.__student)

    def change_value(self,value):
        self.__student = value

i1 = oneneuron()
i1.students()
i1.change_value("Machine Learning")
i1.students()
