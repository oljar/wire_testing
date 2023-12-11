class Geek:
    def __init__(self, age):

        self.age = age

        # getter method
    @property
    def age(self):
        return self.__age

        # setter method

    @age.setter
    def age(self, x):
        self.__age = x


raj = Geek(4)

raj.age =3
raj = Geek(41)
# setting the age using setter
print(raj.age)

# retrieving age using getter

