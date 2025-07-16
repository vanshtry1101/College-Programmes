'''wap prog to create dictionary at run time'''

d={}

# n=int(input("How Many Keys You Want Enter="))

# for i in range(n):
#     key=input("Enter Name=")
#     val=input("Enter Sub=")
#     d[key]=val
# print(d)    


n=int(input("How Many Player You Want Enter="))

for i in range(n):
    key=input("Enter Name=")
    val=input("Enter Score=")
    d[key]=val
print(d)  