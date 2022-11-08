a=int(input())
b=[]
i=0
j=1
b.append(i)
b.append(j)
for i in b:
    u=b[-1]+b[-2]
    b.append(u)
    if u>a:
        break
l=abs(a-b[-1])
k=abs(a-b[-2])
if l>k:
    print(b[-2])
elif l==k:
    print(b[-2],b[-1])
else:
    print(b[-1])

    
    