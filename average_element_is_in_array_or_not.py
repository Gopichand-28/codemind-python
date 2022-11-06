a=int(input())
b=list(map(int,input().split()))
u=0
for i in b:
    u+=i
n=len(b)
p=u//n
if p in b:
    print(True)
else:
    print(False)
    