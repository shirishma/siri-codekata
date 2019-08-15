import re
s=str(input())
x=True
while x:
    if not re.search("[a-z]",s):
        break
    elif not re.search("[0-9]",s):
        break
    else:
        print("yes")
        x=False
        break
if x:
    print("no")
