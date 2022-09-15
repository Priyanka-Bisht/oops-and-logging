class Person:
    def __init__(pink,name,surname,email,YOB):
        pink.name1 = name
        pink.surname = surname
        pink.email = email
        pink.YOB = YOB

    def age(pink,current_year):
        return current_year - pink.YOB

# init is a constructor and pink is a pointer towards classes.

anuj_var = Person("anuj","bhandari","anuj@gmail.com",1994)
pink_var = Person("pink","bisht","pink@gmail.com",1999)
vin_var = Person("vin","balodi","von@gmail.com",1997)
print(pink_var.age(2022))


# print(anuj_var.name1)
# print(anuj_var.surname)
# print(anuj_var.email)
# print(pink_var.name1)
# print(vin_var.surname)
# print(pink_var.email)
