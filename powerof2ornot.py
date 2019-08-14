n=int(input())
p=int(n//2)
for i in range(1,p):
    t=2**i
    if(t==n):
        print("yes")
        break
else:
    print("no")

        
    

        

