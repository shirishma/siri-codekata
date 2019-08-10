n=str(input())
num=0
a=0
sp=0
for i in range(len(n)):
    if(n[i].isdigit()):
        num+=1
    elif(n[i].isalpha()):
        a+=1
    else:
        sp+=1
print(sp)
