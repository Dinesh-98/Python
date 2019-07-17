n=int(input("Enter the number of elements to be in the list:"))
lst=[]

for i in range(n):
    x=int(input())
    lst.append(x)

def sum(lst):
    sum=0
    for i in range(n):
        sum+=lst[i]
    return sum    

def avg(a,n):
    average=a/n
    return average
    

a=sum(lst)
print(avg(a,n))