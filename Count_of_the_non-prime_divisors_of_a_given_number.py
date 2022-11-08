def prime(a):
    cnt=0
    for i in range(1,a+1):
        if a%i==0:
            cnt+=1
    if cnt<=2:
        return a
    else:
        return False
w=int(input())
p=[]
for i in range(1,w+1):
    if w%i==0:
        p.append(i)
y=[]
o=[]
for i in p:
    if i!=1 and  prime(i):
        y.append(i)
    else:
        o.append(i)
print(len(o))