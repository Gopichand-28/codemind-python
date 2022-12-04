def prime(a):
    if a==1:
        return False
    for i in range(2,int(a**0.5)+1):
        if a%i==0:
            return False
    return True
a=int(input())
l=list(map(int,input().split()))
u=int(input())
k=[]
for i in l:
    if prime(i) and i<=u:
        k.append(i)
print(len(k))