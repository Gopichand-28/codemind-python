a=int(input())
b=list(map(int,input().split()))
u=0
for i in b:
    if i%2==0:
        u+=i
print(u)