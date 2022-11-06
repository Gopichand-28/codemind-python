a=int(input())
b=list(map(int,input().split()))
u=0
h=0
for i in b:
    if i%2==0:
        u+=i
    else:
        h+=i
print(abs(u-h))
    