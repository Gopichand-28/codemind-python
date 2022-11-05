a,b=map(int,input().split())
c=[]
for i in range(1,a+1):
    if a%i==0:
        c.append(i)
d=[]
for j in range(1,b+1):
    if b%j==0:
        d.append(j)
p=set(c).intersection(d)
print(max(p))