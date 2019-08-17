n=int(input())
for i in range(1,11):
    if((n+i)%10==0):
        near=n+i
        break
print(near)        
