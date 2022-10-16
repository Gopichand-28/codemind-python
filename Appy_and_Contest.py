t=int(input())
for i in range(t):
    n,a,b,k=map(int,input().split())
    p=n//a
    i=n//b
    if p>=k or i>=k:
        print("Win")
    else:
        print("Lose")
