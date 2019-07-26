N,A,D=map(int,input().split())
a=[1]
for i in range(1,N):
    x=A+i*D
    a.append(x)
s=sum(a)
print(s)
    
