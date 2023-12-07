import datetime
import random

l=[1,2,3,1,4,3,2,9,8,9,7,5]
temp = []
for i in l:
    if i not in temp:
        temp.append(i)
print(temp)
# print(i)
list1 = ["apple","mango","orange","pineapple"]
for a in list1:
    b=0
    for c in a:
        if c in "aeiou":
            b+=1
    print(a,b)
    #function
def functionname():
    print("Welcome")
functionname()
#arguments in function
def sum(a,b):
    print(a+b)

sum(10,20)
#return type
def sum(a,b):
    c=a+b
    return c
sum(10,20)
def mul(c,d):
    e=c*d
    print(e)
mul(20,30)
#math methods
import  math
x=2.2
print(math.ceil(x))
x=10
print(math.fabs(x))
x=5
print(math.factorial(x))
x=10.4
print(math.floor(x))
x=16
print(math.sqrt(x))
#random method
#datetime
import datetime
z=datetime.datetime.now()
q=z.strftime("%y")
print(q)
#lambda
a=lambda name: (name+2)
print(a(2))
v=lambda a,b:(a*b)
print(v(2,3))
#class and object
class swera:
    def __init__(self,name,age):
       self.name=name
        # self.age=age
s = swera("swera", 22)
print(s.name)
print(s.age)