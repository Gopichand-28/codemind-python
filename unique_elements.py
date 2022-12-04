a=int(input())
b=list(map(int,input().split()))
l=[]
for i in b:
    if i not in l:
        l.append(i)
print(*l)
    