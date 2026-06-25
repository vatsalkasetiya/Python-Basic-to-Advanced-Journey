# class student:
#     subject="python"
#     clg="JG"
#     year="Last"
# s2=student()
# s1=student()
# print(s2.subject,s2.clg,s2.year)
# print(s1.subject,s1.clg,s1.year)


# class student:
#     subject="python"
#     print(subject)

# obj1=student()

# class Student:
#     def __init__(self,name,cgpa):
#         self.name=name
#         self.cgpa=cgpa
    
#     def get_cgpa(self):
#         return self.cgpa


# obj1=Student("vatsal",9.3)
# obj2=Student("utsav",4.30)

# print(obj1.get_cgpa())
# print(obj2.get_cgpa())


# class employee:
#     def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary
    
#     def get_salary(self):
#         return self.salary

# obj1=employee("vatsal",50000)
# print(obj1.name,obj1.salary)


# class Car:
#     def __init__(self,car_brand,car_price):
#         self.car_brand=car_brand
#         self.car_price=car_price
    
#     def show_details(self):
#         print("car brand is:",self.car_brand)
#         print("car price is:",self.car_price)

# obj1=Car("BMW",9000000)
# obj1.show_details()




# class Mobile:
#     def __init__(self,brand,ram):
#         self.brand=brand
#         self.ram=ram
    
#     def upgrade_ram(self):
#         self.ram=self.ram+4
    
#     def show(self):
#         print("brand is:",self.brand)
#         print("ram is:",self.ram)

# obj1=Mobile("apple",8)
# obj1.upgrade_ram()
# obj1.show()

# class BankAccount:

#     def __init__(self,owner_name,balance):
#         self.owner_name=owner_name
#         self.balance=balance
    
#     def deposite(self,balance):
#         self.balance=self.balance+balance
        
    
#     def withdraw(self,balance):
#         self.balance=self.balance-balance

#     def show_balance(self):
#         print(self.balance)

# obj1=BankAccount("vatsal",1000)
# obj1.show_balance()
# obj1.deposite(500)
# obj1.show_balance()
# obj1.withdraw(300)
# obj1.show_balance()

# class Student:
#     college="Adani University"

#     @classmethod
#     def show(cls):
#         print(cls.college)
    
# Student.show()

# class Calculator:

#     @staticmethod
#     def add():
#         print(10+20)
# Calculator.add()
# obj=Calculator()
# obj.add()


# class Store:
#     count=0
#     def __init__(self,product_name,product_price):
#         self.product_name=product_name
#         self.product_price=product_price
#         Store.count+=1
    
#     def get_info(self):
#         print("product name is:",self.product_name,"product price is:",self.product_price)

#     @classmethod
#     def get_Count(cls):
#         print(cls.count)

    
# obj1=Store("iphone",10000)
# obj2=Store("apple",35000)
# obj3=Store("apple",35000)
# obj1.get_info()
# Store.get_Count()

# class Person:
#     def __init__(self,age):
#         self.__age=age
    
#     def set_age(self,age):
#         self.__age=age
    
#     def get_age(self):
#         return self.__age

# obj=Person(10)
# obj.set_age(21)
# print(obj.get_age())


# class Employee:
#     def __init__(self,salary):
#         self.__salary=salary
    
#     def increase_salary(self,amount):
#         self.__salary+=amount
    
#     def show_salary(self):
#         return self.__salary

# obj=Employee(50000)
# print(obj.show_salary())
# obj.increase_salary(10000)
# print(obj.show_salary())


# class Mobile:
#     def __init__(self,battery):
#         self.__battery=battery
    
#     def charge(self,amount):
#         self.__battery+=amount
    
#     def show(self):
#         return self.__battery

# obj=Mobile(50)
# obj.charge(20)
# print(obj.show())

# class BankAccount:

#     def __init__(self,balance):

#         self.__balance=balance


#     def deposit(self,amount):

#         self.__balance+=amount


#     def withdraw(self,amount):

#         if self.__balance>=amount:

#             self.__balance-=amount

#         else:

#             print("Insufficient balance")


#     def show(self):

#         return self.__balance



# obj=BankAccount(1000)

# obj.deposit(500)

# obj.withdraw(5000)

# print(obj.show())


# class Employee:
#     start_time="10AM"
#     end_time="5PM"

#     def change_time(self,new_time):
#         self.end_time=new_time

# class Teacher(Employee):
#     def __init__(self,subject):
#         self.subject=subject

# obj=Teacher("maths")
# obj.change_time("50PM")
# print(obj.subject,obj.start_time,obj.end_time)

# class Vehicle:
#     def start(self):
#         print("vehicle started")
    
# class Car(Vehicle):
#     def drive(self):
#         print("car is driving")

# obj=Car()
# obj.start()
# obj.drive()

# class Person:
#     def show_name(self):
#         print("vatsal")
    
# class Stundet(Person):
#     def show_course(self):
#         print("python")

# obj=Stundet()
# obj.show_name()
# obj.show_course()

# class Grand_Father:
#     def show_grandfather(self):
#         print("i am grand father")

# class Father(Grand_Father):
#     def show_father(self):
#         print("i am father")

# class Son(Father):
#     def show_son(self):
#         print("i am son")

# obj=Son()
# obj.show_grandfather()
# obj.show_father()
# obj.show_son()

# class Father:
#     def car(self):
#         print("father has a car")
# class Mother:
#     def bike(self):
#         print("mother has a scooty")

# class Child(Father,Mother):
#     print("i have both bike and car")

# obj=Child()
# obj.bike()
# obj.car()


# class Teacher:
#     def teach(self):
#         print("teacher teach")

# class Singer:
#     def sing(self):
#         print("singer sing")

# class Person(Teacher,Singer):
#     def work(self):
#         print("person works")

# obj=Person()
# obj.work()
# obj.teach()
# obj.sing()


# class Animal:
#     def eat(self):
#         print("animal class")

# class dog(Animal):
#     def bark(self):
#         print("dog class")

# class cat(Animal):
#     def meow(self):
#         print("cat class")

# obj1=dog()
# obj1.eat()
# obj1.bark()

# obj2=cat()
# obj2.eat()
# obj2.meow()

# class Person:
#     def show_name(self):
#         print("my name is vatsal")

# class Student(Person):
#     def study(self):
#         print("Student studies")

# class Employee(Person):
#     def work(self):
#         print("Employee works")

# obj1=Student()
# obj1.show_name()
# obj1.study()

# obj2=Employee()
# obj2.show_name()
# obj2.work()

# class Parent:
#     def __init__(self):
#         print("hello i am parent")
    
# class Child(Parent):
#     def __init__(self):
#         super().__init__()
#         print("i am child")

# obj=Child()

# class Parent:
#     def show(self):
#         print("i am parent")

# class Child(Parent):
#     def sett(self):
#         super().show()
#         print("i am son")

# obj=Child()
# obj.sett()

# class Person:
#     def __init__(self,name):
#         self.name=name

#     def show_name(self):
#         print("my name is:",self.name)

# class Student(Person):
#     def __init__(self,name,course):
#         super().__init__(name)
#         self.course=course
    
    
#     def show_course(self):
#         print("my course is:",self.course)

        
# obj=Student("vatsal","python")
# obj.show_name()

# obj.show_course()


# class Animal:
#     def __init__(self,animal_name):
#         self.animal_name=animal_name
#     def show_name(self):
#         print("name of animal is:",self.animal_name)

# class dog(Animal):
#     def __init__(self, animal_name,color):

#         super().__init__(animal_name)
#         self.animal_color=color

#     def show_color(self):
#         print("animal color is:",self.animal_color)
        
# obj=dog("horse","black")
# obj.show_color()
# obj.show_name()

# class vehicle:
#     def start(self):
#         print("Vehicle Started")

# class car(vehicle):

#     def start(self):
#         super().start()
#         print("Car Started")

# obj=car()
# obj.start()


# class Animal:
#     def sound(self):
#         print("animal sound")

# class Dog(Animal):
#     def sound(self):
#         print("dog sound")

# obj1=Animal()
# obj2=Dog()
# obj1.sound()
# obj2.sound()

class Shape:
    def draw(self):
        print("Drawing Shape")
class Circle(Shape):
    def draw(self):
        print("Drawing Circle")
class Square(Shape):
    def draw(self):
        print("Drawing Square")
obj1=Circle()

obj2=Square()

obj1.draw()

obj2.draw()