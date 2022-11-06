a=int(input())
b=list(map(int,input().split()))
c=int(input())
cnt=0
for i in b:
    if i==c:
       cnt+=1
if cnt>=1:
    print(True)
else:
    print(False)
       