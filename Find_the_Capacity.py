a,b,c=map(int,input().split())
cap=2*b*a*c*512
i=cap//1024
l=[]
l.append(i)
k=""
k+="KB"
l.append(k)
for j in l:
    print(j,end="")