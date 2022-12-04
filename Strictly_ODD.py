a=int(input())
l=list(map(int,input().split()))
k=[]
for i in l:
    if i%2==1:
        k.append(i)
for i in k:
    if l.index(i)%2==0:
        print("False")
        break
else:
    print("True")
