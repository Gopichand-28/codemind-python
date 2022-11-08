a=int(input())
b=list(map(int,input().split()))
p=b[::-1]
for i in p:
    if i%2!=0:
        print(i)
        break