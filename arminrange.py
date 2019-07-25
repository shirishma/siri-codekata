m,n=map(int,input().split())
b=str(m)
l=len(b)
t=m
s=n
arm=0
for i in range(m,n):
    while(i>0):
        r=i%10
        arm=arm+pow(r,l)
        i=i/10
    if(arm==i):
        print(i)
    
