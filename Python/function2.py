'''multiple value returning from the function'''

def test():
    a=int(input("Enter A:="))
    b=int(input("Enter B:="))

    return a+b,a-b,a*b,a/b

ans=test()
print(ans)

#or

add,sub,mul,div=test()

print("addition",add)
print("subtraction",sub)
print("multiplication",mul)
print("divison",div)