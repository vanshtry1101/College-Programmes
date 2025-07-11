name=input("Enter Your Name:=")

cnt=0
v=0
l=0
u=0

for ch in name:
    cnt=cnt+1

    if(ch=="a" or ch=="e" or ch=="i" or ch=="o" or ch=="u"):
      v=v+1
    if(ch.islower()):
       l=l+1
    if(ch.isupper()):
       u=u+1  

print("name=",name)
print("Length=",cnt)
print("Vowels=",v)
print("LowerCase=",l)
print("Uppercase=",u)          