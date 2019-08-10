n=int(input())
a=-1
b=1
d=[]
for i in range(n+1):
    c=a+b
    a=b
    b=c
    d.append(c)
d.remove(0)    
print(*d)
