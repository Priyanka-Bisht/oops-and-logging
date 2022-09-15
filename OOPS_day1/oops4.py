class Person:

    def age(self,current_yeat,YOB):
        return current_yeat - YOB

    def email(self,email):
        print("take and mail id form a person and print it _",email)

    def ask_name(self):
        name = input("tell me your name")
        return name

    def ask_dob(self):
        dob = input("tell me your dob")
        return dob

pink = Person()
anuj = Person()
vin = Person()

pink.email("pink@gmail.com")
print(pink.ask_name())

print(himan.ask_name())