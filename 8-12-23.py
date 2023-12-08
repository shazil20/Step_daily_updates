import json

#Method

class Democlass:
    a=10
    def showvalue(self):
        self.c=self.a*self.a
        print(self.c)
    def showvalue1(self):
        print("Welcome")
obj=Democlass()
obj.showvalue()
obj.showvalue1()
constructor
def __int__(self):
        print("hello")
#inheritance
class A:
    def displayA(self):
        print("welcome A")
class B(A):
    def displayB(self):
        print("welcome B")
class C(B):
    def displayC(self):
     print("welcome C")
obj=C()
obj.displayA()
obj.displayB()
obj.displayC()
# #polymorphism
l=[10,20,30,40]
print(len(l))
s="welcome"
print(len(s))

#overloading
class ws:
    def displayinfo(self,name):
        print('WELCOME' +name)
obj=ws()
obj.displayinfo('python')
#overriding
class rs(ws):
    def displayinfo(self):
        super().displayinfo(self)
        print("welcome")
obj=rs()
obj.displayinfo()
#scope
def abc():
     global x
     x=5
abc()
def ghz():
    y=15
    print(x+y)
ghz()
import json
x={
   "name":"sawera",
   "age":"19",
   "course":"python"
}
y=json.dumps(x)
print(y)
import json

x = {
   "name": "sawera",
   "age": "19",
   "course": "python"
}

y = json.loads(x)
print(y["age"])

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x},{self.y})"

    def __str__(self):
        return f"({self.x},{self.y})"


point = Point("3", "2")
print(repr(point))
print(str(point))
