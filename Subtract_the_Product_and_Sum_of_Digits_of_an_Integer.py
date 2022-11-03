a=int(input())
p=0
o=1
while a>0:
    s=a%10
    p=s+p
    o=o*s
    a=a//10
e=abs(p-o)
print(e)