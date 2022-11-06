a=int(input())
b=list(map(int,input().split()))
p=0
for i in b:
    if i%2!=0:
        p+=i
print(p)
        