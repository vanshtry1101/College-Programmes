file=open("file1.txt","r")
data=file.read()
cnt=cnt=0
u=0
s=0
l=0
a=0
v=0
d=0

for i in data:
    cnt=cnt+1

    if(i=="a" or i=="e" or i=="i" or i=="o" or i=="u" or i=="A" or i=="E" or i=="I" or i=="O" or i=="U"):
        v=v+1
    if(i.islower()):
        l=l+1
    if(i.isupper()):
        u=u+1
    if(i.isdigit()):
        d=d+1
    if(i.isalpha()):
        a=a+1
    if(i.isspace()):
        s=s+1
print("Number Of Ch IS:=",cnt)
print("Number Of Vowels IS:=",v)
print("Number Of Lower Ch IS:=",l)
print("Number Of Upper Ch IS:=",u)
print("Number Of digit IS:=",d)
print("Number Of Alpha IS:=",a)
print("Number Of Space IS:=",s)
