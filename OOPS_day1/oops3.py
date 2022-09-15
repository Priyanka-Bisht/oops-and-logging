class Person:
    def __init__(pink,name,surname,email,YOB):
        pink.name1 = name
        pink.surname = surname
        pink.email = email
        pink.YOB = YOB

    def __init__(pink,name,surname):
        pink.name1 = name
        pink.surname = surname

    def age(pink,current_year):
        return current_year

anuj_var = Person("anuj","bhandari")
pink_var = Person("pink","bisht")
vin_var = Person("vin","balodi")

print(anuj_var.age(2022))
print(pink_var.age(2022))



