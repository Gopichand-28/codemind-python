a=int(input())
b=list(map(int,input().split()))
c,d=map(int,input().split())
s=0
for i in range(a):
    if c>b[i] or d<b[i]:
        s+=b[i]
print(s)
