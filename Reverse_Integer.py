def integer(a):
    s=0
    while a>0:
        d=a%10
        s=s*10+d
        a=a//10
    return s
a=int(input())
k=0
if a<0:
    k=a*(-1)
    j=integer(k)
    print(j*(-1))
else:
    u=integer(a)
    print(u)