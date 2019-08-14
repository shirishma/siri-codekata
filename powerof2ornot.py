n=int(input())
p=int(n//2)
for i in range(1,p):
    temp=2**i
    if(temp==n):
        print("yes")
        break
else:
    print("no")

        
    

        

