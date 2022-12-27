a=int(input())
l=list(map(int,input().split()))
o=[]
k=[]
for i in l:
    if i%2==0:
        o.append(i)
    else:
        k.append(i)
j=[]
x=0
if len(o)==len(k):
    for i in range(len(o)):
        j.append(o[i])
        j.append(k[i])
    print(*j)
elif len(k)>len(o):
    x=k[len(o)::]
    for i in range(len(o)):
        j.append(o[i])
        j.append(k[i])
    if len(x)%2!=0:
        x.append(0)
    j+=x
    print(*j)
elif len(o)>len(k):
    x=o[len(k)::]
    for i in range(len(k)):
        j.append(o[i])
        j.append(k[i])
    if len(x)%2!=0:
        x.append(0)
    j+=x
    print(*j)
        