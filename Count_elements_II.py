a,b=map(int,input().split())
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
k=[]
for i in l1:
    if i  not in l2:
        k.append(i)
for j in l2:
    if j  not in l1:
        k.append(j)
t=[]
for i in k:
    if i not in t:
        t.append(i)
print(len(t))