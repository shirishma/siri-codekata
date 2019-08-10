s,u=map(int,input().split())
s=s^u
u=s^u
s=s^u
print(s,u)
