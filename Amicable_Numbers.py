a=int(input())
b=int(input())
y=0
z=0
for i in range(1,a):
    if a%i==0:
        y=y+i
for j in range(1,b):
    if b%j==0:
        z=z+j
if y==b and z==a:
    print('Amicable')
else:
    print('Not Amicable')
    
        