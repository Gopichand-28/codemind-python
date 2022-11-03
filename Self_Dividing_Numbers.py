def selfdiv(b):
    o=b
    p=[]
    while o>0:
        s=o%10
        p.append(s)
        o=o//10
    n=len(p)
    cnt=0
    for i in p:
        if i!=0 and b%i==0:
            cnt+=1
    if n==cnt:
        return True
    else:
        return False

a=int(input())
b=int(input())
u=[]
for i in range(a,b+1):
    if selfdiv(i):
        u.append(i)
    else:
        pass
for i in u:
    print(i,end=" ")
