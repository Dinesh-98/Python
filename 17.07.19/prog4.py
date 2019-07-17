x=2
y=int(input("Enter the number of optional arguments:"))
lst=[]
lst1=[]
for i in range(y):
    a=int(input())
    lst.append(a)

for i in range(y):
    b=x**2 + lst[i]**2
    lst1.append(b)

print(lst1)    