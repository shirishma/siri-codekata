n=str(input())
f=0
for i in range(len(n)):
    if(n[i]=='0' or n[i]=='1'):
        f=1
if(f==1):
    print("yes")
else:
    print("no")
    
