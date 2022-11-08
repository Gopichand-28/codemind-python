a=int(input())
v=[]
i=0
j=1
v.append(i)
v.append(j)
for i in v:
    g=v[-1]+v[-2]
    v.append(g)
    if len(v)==a:
        break
print(*v)
    