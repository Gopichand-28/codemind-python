a=int(input())
y=0
while a>0:
    s=a%10
    y=y+s
    a=a//10
    if a==0 and y>9 :
        a=y
        y=0
print(y)