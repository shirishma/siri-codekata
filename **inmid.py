s=input()
l=len(s)
k=l//2
if(l%2==1):
    print(s[:k]+"*"+s[k+1:])
else:
    print(s[:k-1]+"**"+s[k+1:])
