# OOPS Practice questions

# Create a Class with instance attributes-Write a Python program to create a Vehicle class with max_speed and mileage instance attributes.
class Vehical:
    def __init__(self,max_speed,mileage):
        self.max_speed = max_speed
        self.mileage = mileage

car1 = Vehical('100kmph',200)
print(car1.mileage,car1.max_speed)





# Create a Vehicle class without any variables and methods
class Vehical:
    pass

# Create a child class Bus that will inherit all of the variables and methods of the Vehicle class
class Vehical:
    def __init__(self,name,max_speed,mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehical):
    pass

School_bus = Bus("school-volvo",200,180)
print(School_bus.name,School_bus.max_speed,School_bus.mileage)




# clss inheritance
class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"

class Bus(Vehicle):
    # assign default value to capacity
    def seating_capacity(self, capacity=50):
        return super().seating_capacity(capacity=50)
school_bus = Bus("school_volvo",180,50)
print(school_bus.seating_capacity())




# Define a property that must have the same value for every class instance (object)
class Vehicle:
    # class attribute
    color = "White"

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass

class Car(Vehicle):
    pass

school_bus = Bus("school_volvo",150,200)
print(school_bus.color,school_bus.mileage,school_bus.max_speed,school_bus.name)

car = Car("Audi",250,450)
print(car.name,car.mileage,car.color,car.max_speed)



# Class Inheritance - Create a Bus child class that inherits from the Vehicle class. The default fare charge of any vehicle is seating capacity * 100.
# If Vehicle is Bus instance, we need to add an extra 10% on full fare as a maintenance charge. So total fare for bus instance will become the final
# amount = total fare + 10% of the total fare.
class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    def fare(self):
        return self.capacity * 100

class Bus(Vehicle):
    def fare(self):
        amount = super().fare()
        amount += amount*10/100
        return amount

School_bus = Bus("School Volvo", 12, 50)
print("Total Bus fare is:", School_bus.fare())




# Check type of an object
class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

class Bus(Vehicle):
    pass

School_bus = Bus("School Volvo", 12, 50)
print(type(school_bus))



# Determine if School_bus is also an instance of the Vehicle class
class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

class Bus(Vehicle):
    pass

School_bus = Bus("School Volvo", 12, 50)
print(isinstance(school_bus, Vehicle))


# Python OOPs Exercise 1: Write a Program to create a class by name Students, and initialize attributes like name, age, and grade while creating an object.
class Student:
    def __init__(self,name,age,grade):
        self.name = name
        self.age = age
        self.grade = grade
rajneesh = Student("Rajneesh",15,"12th-A")
print(rajneesh.grade)


# Python OOPs Exercise 3: Write a program, to create a child class Teacher that will inherit the properties of Parent class Staff
class Staff:
    def __init__(self,role,dept,salary):
        self.role = role
        self.dept = dept
        self.salary = salary

    def staff_details(self):
        print("Name:",self.name)
        print("Age:",self.age)
        print("Role:",self.role)
        print("Department:",self.dept)
        print("Salary",self.salary)

# inherit from class staff
class Teacher(Staff):
    def __init__(self,name,age):
        self.name = name
        self.age = age
        # inherit from parent class
        super().__init__("Teacher","Science",50000)

saurabh = Teacher("Saurabh",40)
saurabh.staff_details()


# Python OOPs Exercise 4: Write a Program, to create a class and using the class instance print all the writable attributes of that object.
class Staff:
    def __init__(self,role,department,salary):
        self.role = role
        self.department = department
        self.salary = salary

    def show_details(self):
        print("Name:",self.name)
        print("Age:",self.age)
        print("Role:",self.role)
        print("Department:",self.department)

# inherit from class Staff
class Teacher(Staff):
    def __init__(self,name,age):
        self.name = name
        self.age = age
        # inherit from Parent class
        super().__init__("Teacher","Mathematics",45000)

sargun = Teacher("Sargun",25)
print(sargun.__dict__)


# Python OOPs Exercise 5: What would be the output of the following program?
class Staff:
    def __init__(self, role, dept, salary):
        self.role = role
        self.dept = dept
        self.salary = salary

    def show_details(self):
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("Role:", self.role)
        print("Department", self.dept)

#inherit from the Staff class
class Teacher(Staff):
    def __init__(self, name, age):
        self.name = name
        self.age = age

        # initialize the Parent  class
        super().__init__("Teacher", "Science", 25000)

teacher = Teacher("Raj", 45)

print(isinstance(teacher, Teacher))
print(isinstance(teacher,Staff))


# Python OOPs Exercise 6: Create a class Teacher with name, age, and salary attributes, where salary must be a private attribute that cannot be accessed outside the class.
class Teacher:
    def __init__(self,name,age,salary):
        self.name = name
        self.age = age
        # private variable
        self.__salary = salary

    def show_details(self):
        print("Name:",self.name)
        print("Age:",self.age)
        # access private attribute inside the class
        print("Salary:",self.__salary)

astha = Teacher("Astha",23,25000)
astha.show_details()

print(astha.name)   #Astha
print(astha.age)
#print(astha.__salary)
#access private member outside the class will throw error


#Python OOPs Exercise 7: Write a Python program that overloads the operator + and > for a custom class.
class Orders:
    def __init__(self,items):
        self.items = items

    def __add__(self, other):
        return self.items + other.items

    def __gt__(self, other):
        return len(self.items) > len(other.items)

order1 = Orders([9,13,15,29,30,17,22,12,16,25])
order2 = Orders([20,92,98,87,68])
print("order1+order2:",order1+order2)
print("order1>order2:",order1>order2)



#Python OOPs Exercise 8: Write a Python program that checks if one class is a subclass of another?
class Teacher:
    def __init__(self,name,age):
        self.name = name
        self.age = age

class Staff(Teacher):
    def show_details(self):
        print("Name:",self.name)
        print("Age:",self.age)

print("Is Teacher a subclass of Staff:",issubclass(Teacher,Staff))
print("Is Staff a subclass of Teacher:",issubclass(Staff,Teacher))


# Python OOPs Exercise 9: Write a Python program that lists out all the default as well as custom properties of the class.
class Teacher:
    def __init__(self,dept,salary,specialization):
        self.dept = dept
        self.salary = salary
        self.specialization = specialization

jaya = Teacher("Forestry",65000,"antomony")
print(dir(Teacher))



# Python OOPs Exercise 10: Write a Program in Python to implement a Stack Data Structure using Class and Objects, with push, pop, and traversal method.
class Stack:
    # initialize an empty list
    def __init__(self):
        # conventional private member
        self.__stack = []

    def push(self,items):
        self.__stack.append(items)

    def pop(self):
        self.__stack.pop()

    def traverse(self):
        for i in self.__stack[::-1]:
            print("|", i ,"|")
# initialize the object
stack = Stack()

# Push items to the stack
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)
stack.push(6)
stack.push(7)
stack.push(8)

# pop items from the stack
stack.pop()
stack.pop()

# traverse through the stack
stack.traverse()



# Python OOPs Exercise 11: Write a program that prints the class name using its object.
# Solution. Using the object’s __class__.__name__ property we can access the class Name of the object.

class Animal:
    pass
lion = Animal()
print("The charcteristics of the lion object is:",lion.__class__.__name__)


# Python OOPs Exercise 11: Write a Python class Square, and define two methods that return the square area and perimeter.
class Square:
    def __init__(self,a):
        self.a = a

    def area(self):
        return self.a*self.a

    def perimeter(self):
        return 4*self.a

# initialize the object of class square
square1 = Square(10)
square2 = Square(20)

print("Area of square1:", square1.area())
print("Perimeter of square2:",square1.perimeter())

print("Area of square1:", square2.area())
print("Perimeter of square2:",square2.perimeter())

