n=int(input())
while(n<=1000):
    for i in range(2,n/2):
        if(n%i==0):
            print("no")
        else:
            print("yes")
            
            
            
