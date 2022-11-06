a=int(input())
r=0
s=[]
for i in range(1,a):
    if a%i==0:
        r+=i
        s.append(i)
y=sum(s)
if y>a:
    print("True")
else:
    print("False")
