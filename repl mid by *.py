s=str(input())
if(len(s)%2==0):
    for i in range(len(s)):
        if(i==len(s)//2-1):
            s=s[:i]+"**"+s[i+2:]
else:
    for i in range(len(s)):
        if(i==len(s)//2):
            s=s[:i]+"*"+s[i+1:]
print(s)                
        
