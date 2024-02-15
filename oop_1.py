# # class Car: 
# #     name = "Honda"
# #     price = 200000
# #     max_speed = "200 km/hr"

# # car1 = Car()
# # car2 = Car()
# # car2.name = "Suzuki"
# # car3 = Car()

# # print(car1.name)
# # print(car2.name)
# # print(car3.name)


# class Bike:
#     name = "Pulsar"
#     price = 400000
#     colour = "black"

# class Car: 
#     name = "Honda"
#     price = 200000
#     max_speed = "200 km/hr"

#     def get_name(self):     #prints the "name" attributes data from the same class 
#         print(self.name)
    
#     def set_name(self,names):
#         self.name = names
#         self.get_name()

# car1 = Car()
# car1.set_name("Tata")
# print(car1.name)

# class Car: 
    
    
#     def __init__(self,name,price, max_speed):
#         self.name = name
#         self.price = price
#         self.max_speed = max_speed

# car1 = Car("ferrari","1.2 million", "300 km/hr")



# print(car1.__dir__())

# a = 3
# b = 4

# print(a.__add__(b))


# class Car: 
    
    
#     def __init__(self,name,price, max_speed):
#         self.name = name
#         self.price = price
#         self.max_speed = max_speed

#     def __str__(self) -> str:
#         return self.name

# car1 = Car("Ferrari","1.2 million", "300 km/hr")

# print(car1)

# class Vehicle:
#     wheels = None
#     speed = None
#     price = None

#     def set_wheels(self, wheels):
#         self.wheels = wheels
#         print(self.wheels)

# class Car(Vehicle):
#     pass
    
# car1 = Car()
# print(car1.wheels)
# car1.set_wheels(4)

#     polymorphism 

# class Cow:
#     def move(self):
#         print("It is walking")

# class Fish:
#     def move(self):
#         print("It is swimming")

# class Bird:
#     def move(self):
#         print("It is flying")

# cow1 = Cow()
# fish1 = Fish()
# bird1 = Bird()

# cow1.move()
# bird1.move()
# fish1.move()


#    Abstraction
# from abc import ABC, abstractmethod

# class Animal(ABC):

#     @abstractmethod
#     def move(self):
#         # print("It is moving")
#         pass

# class Cow(Animal):
#     def move(self):
#         print("It is walking")


# cow1 =  Cow()
# cow1.move()

#   Encapsulation 

# class User:
#     def __init__(self,email,password):
#         self.email = email
#         self.__password = password

#     def get_password(self):
#         print(self.__password)

# user1 = User("ram@gmail.com", "ram123")

# user1.get_password()

# def hello(func):
#     print("Hello welcome")
#     func()

# @hello
# def hello_world():
#     print("Hello world")
