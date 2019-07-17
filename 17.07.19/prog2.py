lst=[]
n=int(input("Enter the number of elements in the list:"))
for i in range(n):
    x=int(input())
    lst.append(x)  
#print(min)    
def minimum(lst):
    min=lst[0]
    for i in range(0,n-1):
        j=i+1
        if lst[i]>lst[j] and lst[j]<min:
            min=lst[j]
    return min           

print(" ")
print(minimum(lst))