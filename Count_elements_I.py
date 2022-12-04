a,b=map(int,input().split())
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
k=[]
for i in l1:
    if i in l2:
        k.append(i)
t=[]
for i in k:
    if i not in t:
        t.append(i)
print(len(t))
        
        