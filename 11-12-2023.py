# number of duplicates in list
list = [10,20,30,10,40,50,10,20,50,40]
temp = []
for x in list:
    if list.count(x) > 1 and x not in temp:
        temp.append(x)

y = len(temp)
print(y)
temp2 = []
for l in list:
    print(l)
    for m in list:
        if list.count(m) > 1 and m not in temp2:
            temp2.append(m)
n = len(temp2)
print(n)



name = "shazil"
sam = f"hello {name}"
print(sam)

name = input("Enter your age : ")
year = int(name)
months = year * 12
days = year * 365
print(f"Your age {year} is equal to {months} months and {days} days.")

a = {2,3,5,4}
b = {2,3,5}
c = a.difference(b)
print(c)

user_input = input("Enter y for 'Yes' and n for 'No' (y/n) : ")
if user_input == "y":
    o = range(3)
    for x in o:
        print("False")
elif user_input == "n":
    i = 1
    while i<=5:
        print("correct")
        i +=1
else:
    print("Answer in y/s")


list1 = [1,2,3,4,50,60,9]
for x in list1:
    print(x)
i =1
while i<=5:
    i = int( input("Enter 5 values : "))
    i+=1



list5 = ["shazil","ali","moez"]
list6 = [x *2 for x in  list5]
print(list6)
list7 = [list1 for list1 in range(0,100)]
print(list7)

list8 = []
for list8 in  range(100):
    print(list8)