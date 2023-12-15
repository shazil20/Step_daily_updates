# type hinting
def show(value:str):
    print(value)
    print(value.upper())
show("abc,gfr")
def sum(a:int,b:int):
    print("adding two numbers")
    return a+b
sum(12,3)




abn = 12
bbn = 11

if abn == bbn:
    print("Correct")
else:
    pass
# first class function
def sum(fun,a,b):
    result = fun(a, b)
    return result
def divid(x,y):
    return x/y
a = 3
b = 5

# sum1 = sum(divid,a,b)
# print(sum1)
#
#
# def divs(x,y):
#     z = x/y
#     print(z)
#     if z == 0:
#         raise ZeroDivisionError()
# divs(4,0)
# decorators



def decor(fun):
    def inner():
        print("IF:Before enhancing")
        fun()
        print("IF:After enhancing")
    return inner
@decor
def show():
   print("we will use this function")
   print("we will decorate this function")

show()
# modubility
a = 12
b = a

print(a)
