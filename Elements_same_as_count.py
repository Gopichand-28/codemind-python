a=int(input())
b=list(map(int,input().split()))
k=set(b)
p=[]
for i in b:
    if b.count(i)==i:
        p.append(i)
if len(p)==0:
    print("-1")
else:
    l=[]
    for i in p:
        if i not in l:
            l.append(i)
    print(*l)