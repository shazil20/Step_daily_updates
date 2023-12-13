list=[10,20,30,10,40,50,10,20,50,40,10,10,40]
dict={}
for x in list:
    if x in dict:
        dict[x] += 1
    else:
        dict[x] = 1

for y, count in dict.items():
    if count>1:
        print(f"{y}  :  {count}")
# unpacking a function
# def add(usr,age):
#     print(usr,age)
# dic={"usr":"sawera","age":20}
# add(**dic)
# oop
class zero:
   def --init--(self):
      self.name="sawera"
      self.age=20
a=zero()
print(a.name)
print(a.age)