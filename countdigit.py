n=str(input())
b=0
for i in range(len(n)):
    if(n[i].isdigit()):
        b+=1
print(b)
