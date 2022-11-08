a=int(input())
r=[]
i=0
j=1
r.append(i)
r.append(j)
for p in r:
    t=r[-1]+r[-2]
    r.append(t)
    if len(r)==a:
        break
print(*r)
    