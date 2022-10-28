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
        print('Spy Number')
    else:
        print('Not Spy Number')
num=a
spy_number_check(num)
    