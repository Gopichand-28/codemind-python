a=int(input())
b=a*a
y=0
while b>0:
    s=b%10
    y=s+y
    b=b//10
if a==y:
    print('Neon Number')
else:
    print('Not Neon Number')