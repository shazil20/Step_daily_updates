# a = "Hello"
# def myfunction():
#     print(a)
#
# myfunction()
# a = str("shazil")
# print(a.translate())
# a = ["shazil","33","45"]
# print(type(a))
# a = ["A","B","C"]
# b = ["a","b","c"]
# for x in b:
#     a.append(b)
# print(a)
# l = "a"
# j = []
# for j in l:
#     j.split(l)
# print(type(l))
# a = str(12)
# print(type(a))
# a = "shazil"
# print(a)
# s = ["1","2","3"]
# x,y,z = s
# print(x,y,z)
# a = 12
# b = float(a)
# print(type(b))
# a = '''askdlkasjd
# asldjaskdkl
# asslkdjlasj
# '''
# print(len(a))
# a = "shazil is a \"programmer\"."
# print(a)
# b = "shazil rj {}"
# print(b.endswith("rj"))
# print((b.format_map()))
# # remove duplicates
# list1 = [1,2,3,1,4,3,2,9,8,9,7,5]
# list2 = set(list1)
# print(list2)
# list2= list1.copy()
# list2.sort()
# i=0
# while i == list2:
#     i = i + 1
#     print(i)
# print(list2)
# for x in list2:
#     print(x)
#
#
#
#
#
#
#
# for x in list2:
#     print(x)
#
#
# print(list1[0])
#vowels code
list1 = ["apple","mango","orange","pineapple"]
for x in list1:
    y=0
    for z in x:
        if z in "aeiou":
            y +=1
    print(x , y)
