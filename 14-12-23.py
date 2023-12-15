class Student:
    def __init__(self):
        self.name = "Shazil"
        self.grade = (120,130,140)

    def average(self):
        return sum(self.grade) / len(self.grade)


student = Student()
print(Student.average(student))


class frame():
    def instance(self):
        print("this is instance level.")


    @classmethod
    def classmethod(cls):
        print("This is class level.")

    @staticmethod
    def saticmethode():
        print("this is static level.")


f = frame()
print(f.instance())
print(f.classmethod())
print(f.saticmethode())


class Animal1:
    def __init__(self):
        self.dec()

    def dec(self):
        global a
        global b
        a = 12
        b = 10

class Animal2(Animal1):
    def __init__(self):
        super().__init__()
        self.sumo = a + b

an = Animal2()
print(an.sumo)


class Office:
    global a
    global b
    a = 15
    b = 15

class office2(Office):
    sum = a+b
    print(sum)

class Office3(Office):
    sub = a-b
    print(sub)

of = Office()
my_list = [10,10,10,10,10,10,20,20,20,30,30,30,30,30,10,10]
temp = {}
for x in my_list:
    if x in temp:
        temp[x] += 1
        if temp[x] % 1 == 0:
            pairs = temp[x] / 2
            print(f"{x} has {pairs} number of pairs.")
    else:
        temp[x] = 1

for element, count in temp.items():
    if count > 1:
        print(f"{element} have {int(count/2)} pair.")
test case
for x in my_list:
    if x in temp:
        temp[x] += 1
        if temp[x] % 2 == 0:
            pairs = temp[x] // 2
            print(f"{x} has {pairs} pair(s).")
    else:
        temp[x] = 1


my_list = [10, 10, 10, 10, 10, 10, 20, 20, 20, 30, 30, 30, 30, 30, 10, 10]
temp = {}

for x in my_list:
    if x in temp:
        temp[x] += 1
        if temp[x] % 2 == 0 and temp[x] // 2 == 1:
            pairs = temp[x] // 2
            print(f"{x} has {pairs} pair(s).")
    else:
        temp[x] = 1