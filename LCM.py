a,b=map(int,input().split())
i=1
o=[]
while a>0 and i<=1000:
    s=a*i
    o.append(s)
    i+=1
p=1
l=[]
while b>0 and p<=1000:
    v=b*p
    l.append(v)
    p+=1
f=set(o)
n=set(l)
if len(f.intersection(n))>0:
    print(min(f.intersection(n)))
else:
    pass