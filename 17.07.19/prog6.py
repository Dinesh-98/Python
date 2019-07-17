n=int(input())
list1=[]


def fibonacci(n):
    a=0
    b=1
    list1.append(a)
    list1.append(b)
    for i in range(n):
        res=a+b
        list1.append(res)
        a=b
        b=res
    return list1    

print(fibonacci(n))  