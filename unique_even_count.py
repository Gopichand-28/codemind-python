a=int(input())
b=list(map(int,input().split()))
j=set(b)
cnt=0
for i in j:
    if i%2==0:
        cnt+=1
print(cnt)
