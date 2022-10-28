a=int(input())
y=0
d=1
while a>0:
    s=a%10
    y=s+y
    d=d*s
    a=a//10
if y==d:
    print('Spy Number')
else:
    print('Not Spy Number')
    