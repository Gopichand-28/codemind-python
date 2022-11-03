import math
p=int(input())
for i in range(p):
    a=int(input())
    b=math.sqrt(a)
    c=int(b)
    if c%a==b:
        print('True')
    else:
        print('False')
