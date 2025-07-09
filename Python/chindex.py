'''
write a prog to check given character is present in string and also find'''

name=input("Enter The Name:=")
ch=input("Which Character You Want To Find?")

count=0    
le=len(name)
for i in range(0,le):
    if(name[i]==ch):
        print("Character At=",i)
        count=count+1
if(count==0):
    print("Character Is Not Present") 
else:
    print("Character present",count,"times")           

 