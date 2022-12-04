def prime(a):
    if a==1:
        return False
    for i in range(2,int(a**0.5)+1):
        if a%i==0:
            return False
    return True
a=int(input())
l=list(map(int,input().split()))
k=[]
for i in l:
    if prime(i):
        k.append(i)
o=sum(k)/len(k)
print("{:.2f}".format(o))