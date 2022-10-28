a=int(input())
def neon(num):
    b=num*num
    y=0
    while b>0:
        s=b%10
        y=s+y
        b=b//10
    if a==y:
        return True
    else:
        return False
if neon(a):
    print('Neon Number')
else:
    print('Not Neon Number')