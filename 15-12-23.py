class Bookshelf:
    def __init__(self,name):
        self.name = name

class Book(Bookshelf):
    def __init__(self,price, name):
        super().__init__(name)
        self.price = price

book = Book(price="25/-",name = "Animal-Moiz")
print(book.price)
print(book.name)


def divs(x,y):
    z = x/y
    print(z)
    if z == 0:
        raise ZeroDivisionError("runtime error")
divs(4,2)


try:
    x = int(input("Enter a number: "))
    y = int(input("Enter another number: "))
    result = x / y
except ZeroDivisionError:
    print("Cannot divide by zero!")
except ValueError:
    print("Invalid input. Please enter valid numbers.")
else:
    print(f"Division successful! Result: {result}")
finally:
    print("This block always executes.")

my_list = [10, 10,20,20,10,10,20,20]
temp = {}

for x in my_list:
    if x in temp:
        temp[x] += 1
    else:
        temp[x] = 1

output = [f"{key} has {value//2} pairs" for key, value in temp.items()]
print("\n".join(output))
#

def shout(text):
    return text.upper()

print(shout('Hello'))

yell = shout

print(yell('Hello'))