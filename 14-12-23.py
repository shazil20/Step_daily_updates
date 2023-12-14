# dictionary comprehension
# dict={}
# for x in range(10):
#     dict[x]=x*2
#     print(dict)
# other method
# dict2={n:(n if n%2==0 else 'invalid') for n in range(10)}
# print(dict2)
# # unpacking arguments
# def show(a,b,c,d):
#     print(a)
#     print(b)
#     print(c)
#     print(d)
# l=[10,20,30,40]
# show(*l)
#
#
#
# class Frame:
#     def __init__(self):
#         self.name1 = "Sawera1"
#         self.name2 = "Sawera2"
#
#     def __str__(self):
#         return f"Frame: {self.name1}"
#
#     def __repr__(self):
#         return f"Frame(name1={self.name1}, name2={self.name2})"
#
# f = Frame()
# print(str(f))  # This will call __str__
#
# print(repr(f))  # This will call __repr__
# # class inheritance
# class office:
#     global a
#     global b
#     a=5
#     b=5
# class office2:
#     sum=a+b
#     print(sum)
# class office3:
#     mul=a*b
#     print(mul)
# of=office()
# print(of)
# class composition
# super()
# problem
l = [10, 20, 30, 10, 40, 50, 10, 20, 50, 40, 10, 10, 40, 10,20,20]
dict = {}
for x in l:
    if x in dict:
        dict[x] += 1
    else:
        dict[x] = 1

for y, count in dict.items():
    if count > 1:
        print(f"{y}  :  {int(count / 2)}")
