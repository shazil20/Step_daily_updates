# dictionary
a={
    "sawera":20,
    "sheeza":21,
    "minahil":22
}
a["sawera"]=19
print(a)
# list with dictionary
a=[
    {"name":"sawera","age":20},
{"name":"sheza","age":20},
{"name":"minahil","age":20},
    ]
print(a)
# print(a[2])
# use in keyword
d={
    "name":"sawera"
}
if "name" in d.items():
    print("yes")
else:
    print("no")
    #list comprehension
l=["shiza"'"minahil',"hamna"]
a= [m for m in l if m.startswith("s")]
print(a)
# destructuring variables
x,y=3,4
print(x,y)
a={"sawera":20,"shiza":21,"minha":22}
print(list[a.items()])
for x in a.items():
    print(x)
    a={"name":"sawera","age":20}
    print(a.values())

#destructive variable
*head, tail = [1,2,3,4,5,6,7,8,0,43,5,34,2,321,52,54,576]
print(head)
print(tail)
# functions
def hello():
    print("hello")
hello()
# def user():
#     user=input("Enter your age")
#     a=user*364*24*60*60
#     print(a)
# user()
# parameters
def add(x,y):
    print(x+y)
add(2,3)


x = 5
def fun(m,n=x):
    sum = m+n
    print(sum)
fun(2)

def return_42():
    return 42
def my_function(arg1 , arg2):
    return arg1 * arg2
# lambda
print((lambda x,y : x+y) (7,6))
# dictionary comprehension
