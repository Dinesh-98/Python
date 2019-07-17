n=int(input("Enter the number of elements to be in the list:"))
lst=[]
for i in range(n):
    x=int(input())
    lst.append(x)

print(sorted(lst,reverse=True))