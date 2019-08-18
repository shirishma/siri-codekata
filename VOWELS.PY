s=str(input())
l=['a','e','i','o','u']
f=0
for i in range(len(s)):
    if l[i] in s:
        f=1
        break
if f==1:
    print("yes")
else:
    print("no")
