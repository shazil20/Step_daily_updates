# class and objects
class Car:
    def __int__(self, a, b):
        self.a = a
        self.b = b

    def __repr__(self):
        return "this class take 2 values"

    def __str__(self):
        return "this class take 2 values"
    # def __str__(self,a,b):
    #     self.a = a
    #     self.b = b
    #     c=a+b


ca = Car()
print(ca)
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    def __str__(self):
        return f"({self.x}, {self.y})"


# Create an instance of the Point class
point = Point(3, 4)

# Using __repr__
print(repr(point))  # Output: Point(3, 4)

# Using __str__
print(str(point))   # Output: (3, 4)



class Myclass:
    def __repr__(self,a,b):
        self.a = a
        self.b = b
        a=12
        b=11
        return a+b
obj = Myclass()
print(obj)
class MyClass:
    def __init__(self):
        self.a = 12
        self.b = 11

    def __repr__(self):
        return f"MyClass(a={self.a}, b={self.b})"

    def __str__(self):
        return f"(a={self.a}, b={self.b})"

# Create an instance of MyClass
obj = MyClass()

# Print the representation of the object using __repr__
print(obj)
class Myclass:
    a = 12
    b = 11
    c = a+b
    print(c)
class Mylass2(Myclass):
    a = 12
    b = 11
    d = a - b
    print(d)
obj = Myclass()
obj2 = Mylass2()
print(obj)

print(obj2)


#inheritance
class A:
    def displayA(self):
        print("welcome A")
class B(A):
    def displayB(self):
        print('hi B')
class C(B):
    def displayC(self):
        print("python C")
obj=C()
obj.displayA()
obj.displayB()
obj.displayC()



def shazil():
    global x
    x = 23
    print(x)
shazil()

def abc():
    y = 20
    print(x-y)
abc()


mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Drive!")

class Boat:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Sail!")

class Plane:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang")       #Create a Car class
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat class
plane1 = Plane("Boeing", "747")     #Create a Plane class

for x in (car1, boat1, plane1):
  x.move()


import datetime

x=datetime.datetime.now()
print(x)



import math

x = 9.8

print(x.__ceil__())



import json

# a=  '{"name": "Lamborgini","model": "hurrican","year": "2019"}'
a=  {
  "name": "Lamborgini",
  "model": "hurrican",
  "year": "2019"
}
b = json.dumps(a)

print(b)