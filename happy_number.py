def teju_picchi(a):
    s=0
    if a<=9:
        return a==1 or a==7
    while a:
        r=a%10
        s+=r*r
        a=a//10
    return teju_picchi(s)
a=int(input())
print(teju_picchi(a))
        
        