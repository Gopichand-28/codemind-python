a=int(input())
b=a%10
c=a//10
d=c%10
e=c//10
f=e%10
g=e//10
if b%2==0 and d%2==0 and f%2==0:
    print("Even")
elif b%2!=0 and d%2!=0 and f%2!=0:
    print("Odd")
else:
    print("Mixed")