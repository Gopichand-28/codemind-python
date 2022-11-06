def po(a):
    l=0
    while a>0:
        a=a//10
        l+=1
    return l
def spl(num):
    o=0
    i=[]
    while num>0:
        x=num%10
        i.append(x)
        num=num//10
    return i
c=int(input())
p=c**2
y=po(c)#lenth of input
z=po(p)#length of sq input
k=spl(c)# rev split of input
j=spl(p)#rev split of sq input
r=k[::-1]#split of input
u=j[::-1]#split of input
s=[]
for i in u:
    if i in r:
        s.append(i)
    else:
        pass
d=[]
for b in s:
    if b not in d:
        d.append(b)
if r==d:
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")