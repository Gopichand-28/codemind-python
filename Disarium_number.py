a=int(input())
r=a
y=[]
while a>0:
    s=a%10
    y.append(s)
    a=a//10
t=y[::-1]
b=len(t)
j=1
g=0
for i in t:
    g+=i**j
    j+=1
if r==g:
    print("True")
else:
    print("False")