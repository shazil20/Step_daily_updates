a=int(input("Enter the value1"))
b=int(input("Enter the value2"))
print(a+b)
a=int(input("Enter the value"))
if a%2==0:
    print(a, "Even number")
elif a%2!=0:
    print(a, "Odd number")
else:
    print(a, "no")
a="sawera"
b=len(a)
print(b)
for c in range(b):
    print(a[c])
    #fuctions
    r="Welcome"
    s=r.isalpha()
    print(s)

    q = chr(65)
    print(q)
print(10>5)
a=10
b=20
print(id(a),id(b))
c="hello"
d="sawera"
print(c+ "" +d)
l=[]
for a in range(0,101):
    l.append(a)

print(l)

n = [h for h in range(0,101) if h%2==0 ]
print(n)
i=1
while i<=10:
    i=i+1
    print(i)