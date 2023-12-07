# tuple
l = [2,23,4,6,7,23]
l.remove(23)
print(l)

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

thislist1 = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)



# dictoneries
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
    print(x)
print(thisdict.keys())
thisdict["color"]="red"
print(thisdict)

a = {
    "child1":{
        "name":"ali"
    },
    "child2":{
        "name":"moiz"
}
}

print(a["child1"])



# loop
i=0
while i<=3:
    i +=1
    if i==2:
        break
    print(i)
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

# for loop
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

# function
def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")
def mois(x,y):
    print(x+y)
mois(2,8)

def hehe():
    a = 12
    b = 13
    if a<b:
        print("yes")

hehe()
def my_function(**kid):
    print("his first name is " + kid["fname"])
    print("His last name is " + kid["lname"])

my_function(fname = "Shazil", lname = "Rj")



# lambda function
y = lambda x: x**2
print(y(5))



def shazil(*key):
    print("my name is" + key[1])
shazil("a","b","c","d")


# class
class shazil:
    def __init__(self,name,age):
        self.name = name
        self.age = age
s = shazil("shazil", 22)

print(s.name)
print(s.age)