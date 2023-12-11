# string
name = "sawera"
print(name+name)
var1="hi"
var2="hi"
num1=4
num2=4
# string formate
name="sawera"
# greeting="f Hello , {name}"
greeting = f"hello,{name}"
print(greeting)
name="sheeza"
greeting="hello,{}"
a=greeting.format(name)
print(a)
print(a)
a="hello {}, today is {}"
b=a.format("sheeza","monday")
print(b)
# a=input("Enter your name:")
# print(a)



# input
# age = input("enter your age : ")
# year = int(age)
# month = year * 12
# day = year * 36520
# print(f"Your age is {year} and the months are {month} also the days are {day}")
# differnce
a={"saba","sehar","sheeza"}
b={"saba","sehar"}
c=a.difference(b)
# intersection
d=a.intersection(b)
print(c)
print(d)
l=[25,25,50]
t=(4,7)
#booleans
print(5==5)
print(5!=5)
print(5<5)
print(5>5)
#if statement
# a=input("What day of the week is it today?")
# if a=="Monday":
#     print("have a great start of the week")
# elif b=="tuesday":
#     print("its tuesday")
# else:
#     print("false")
    # in keyword
# b={"doraemon","beem","tom and jerry"}
# a=input("what movie you recently watch? ")
# if a in b:
#     print("i have watched")
# else:
#     print("i have not watched")
# number=6
# x=input("Enter if 'y' u  want to play! ")
# if x=="y":
#     print(input("guess the number"))
# if "y"==6:
#     print("correct")
# else:
#     print("wrong")
# loop
l=[10,20,40,60,80]
for x in l:
    print(x)
    i=1
while i<=7:
    print(i)
    i+=1
#list comprehension
l=[1,2,3,4,5]
double=[]
for x in l:
   double.append(l*2)
   print(double)
