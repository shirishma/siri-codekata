s1=input()
s2=input()
if(len(s1)>len(s2)):
    print(s1)
elif(len(s2)>len(s1)):
    print(s2)
else:
    print(s1 or s2)
