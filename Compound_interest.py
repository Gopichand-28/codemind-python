p,t,r=map(int,input().split())
r=p*(pow((1+t/100),r))
i=("%.2f"%r)
print(i)