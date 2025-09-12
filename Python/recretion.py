'''Function Call It Self'''


def fact(n):
    if(n==1):
        return 1
    else:
        x=n*fact(n-1)

    return x

n=int(input("Enter Nuber:="))

ans=fact(n)
print("factorial:=",ans)    