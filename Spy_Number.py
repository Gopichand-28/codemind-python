a=int(input())
def spy_number_check(num):
    y=0
    d=1
    while num>0:
        s=num%10
        y=s+y
        d=d*s
        num=num//10
    if y==d:
        return True
    else:
        return False
if (spy_number_check(a)):
    print('Spy Number')
else:
    print('Not Spy Number')