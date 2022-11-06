a=int(input())
b=list(map(float,input().split()))
u=0
for i in b:
    u+=i
n=len(b)
p=u/n
y=("%.2f"%p)
print(y)