a=int(input())
b=list(map(int,input().split()))
u=0
for i in range(0,len(b),2):
    u+=b[i]
v=0
for i in range(1,len(b),2):
    v+=b[i]
print(abs(u-v))