my_list = [10, 20, 30, 10, 40, 50, 10, 20, 50, 40, 10,10,40]
temp = {}

for x in my_list:
    if x in temp:
        temp[x] += 1
    else:
        temp[x] = 1

for element, count in temp.items():
    if count > 1:
        print(f"{element} is repeated {count} times.")


def add(x,y):
    return x+y

nums = {"x": 15, "y": 25}

print(add(x=nums["x"],y=nums["y"]))


def details(us,ag):
    print(us , ag)


dic = {"us": "shazil", "ag":22}
details(**dic)


class Std:
    def __init__(self):
        self.x = "shazil"

s = Std()
print(s.x)



class ss:
    def __init__(self):
        self.x = "hh"
        self.y = 22

    def __str__(self):
        return "shazil20"
m = ss()
print(m.x)
print(m.y)
print(m)