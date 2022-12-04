a=int(input())
b=list(map(int,input().split()))
k=int(input())
p=[]
for i in b:
    if b.count(i)==k:
        p.append(i)
y=[]
for i in p:
    if i not in y:
        y.append(i)
if len(y)==0:
    print("-1")
else:
    print(*y)