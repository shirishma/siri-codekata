m,n=map(int,input().split())
if(m==n):
    print("yes")   
else: 
    r=m*n
    f=0 
    s=r//2
    for i in range(s):
        sq=i*i
        if(sq==r):
            f=1
if(f==1):
    print("yes")
else:
    print("no")
