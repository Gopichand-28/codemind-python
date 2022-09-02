a,b,c=map(int,input().split())
area=0.25*(-a**4+2*(a*b)**2+2*(a*c)**2-b**4+2*(b*c)**2-c**4)**0.5
b=("%.2f"%area)
print(b)