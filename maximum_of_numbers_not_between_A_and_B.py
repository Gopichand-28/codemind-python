a=int(input())
b=list(map(int,input().split()))
c,d=map(int,input().split())
l=[]
for i in range(a):
    if c>b[i] or d<b[i]:
        l.append(b[i])
if len(l)==0:
    print("-1")
else:
    print(max(l))