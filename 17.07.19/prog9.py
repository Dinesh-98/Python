lst=[]

for i in range(50):
    lst.append(i)

result=filter(lambda x:x%2 != 0, lst)
print(list(result))    