a=int(input())
b=list(map(int,input().split()))
k=set(b)
p=[]
for i in b:
    if b.count(i)==i:
        p.append(i)
l=[]
for i in p:
    if i not in l:
        l.append(i)
print(len(l))