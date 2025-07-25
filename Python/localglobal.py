'''local and global variable function'''

##Local Variable

# def test():
#   a=50
#   c=a+20
#   print(c)

# a=90

# test()  
# print(a)




##Global Variable    (work like a call by reference)

def testt(x):          #local variable
   global b
   b=b+x
   print("b value is:=",b)

b=30
print("b",b)

testt(80)

print("b=",b)