a=int(input())
l=[]
i=0
j=1
l.append(i)
l.append(j)
for i in l:
    f=l[-1]+l[-2]
    l.append(f)
    p=len(l)
    if a in l:
        print("True")
        break
    elif p==a:
        print("False")
        break

