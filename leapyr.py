n=int(input())
if(n%100==0):
    if(n%400==0):
        print("yes")
    else:
        print("no")
elif(n%4==0):
    print("yes")
else:
    print("no")
        
