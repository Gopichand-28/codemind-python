a=int(input())
f=[]
while a>0:
    x=a%10
    f.append(x)
    a=a//10
v=f[::-1]
for i in range(len(v)):
    if v[i]==6:
        v[i]=v[i]+3
        break
for i in v:
    print(i,end='')
