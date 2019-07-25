n=int(input())
b=str(n)
l=len(b)
t=n
arm=0
while(n>0):
    r=n%10
    arm=arm+pow(r,l)
    n=n/10
if(arm==t):
    print("yes")
else:
    print("no")
    
