def prime(a):
    cnt=0
    for i in range(1,a+1):
        if a%i==0:
            cnt+=1
    if cnt<=2:
        return True
a=int(input())
b=int(input())
vnt=0
for i in range(a,b+1):
    if i!=1 and prime(i):
        print(i)
