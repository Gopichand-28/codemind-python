a=int(input())
b=list(map(int,input().split()))
k=set(b)
p=[]
for i in b:
    if b.count(i)==i:
        p.append(i)
o=set(p)
if len(o)==0:
    print("-1")
else:
    l=sum(o)/len(o)
    print("{:.2f}".format(l))