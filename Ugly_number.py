def fact(a):
    k=[]
    for i in range(1,a+1):
        if a%i==0:
            k.append(i)
    return k
def prime(b):
    if b==1:
        return False
    for j in range(2,int(b**0.5)+1):
        if b%j==0:
            return False
    return True
c=int(input())
if c==1:
    print("Ugly Number")
elif c<1:
    print("Not Ugly Number")
else:
    p=fact(c)
    t=[]
    for r in p:
        if prime(r):
            t.append(r)
    for i in t:
        if i>5:
            print("Not Ugly Number")
            break
    else:
        print("Ugly Number")