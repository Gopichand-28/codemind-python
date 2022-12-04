a=int(input())
o=list(map(int,input().split()))
b=set(o)
cnt=0
for i in b:
    if i%2==1:
        cnt+=1
print(cnt)