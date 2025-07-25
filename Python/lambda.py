'''wap a program to find max value from two numbers using lambda(enonimas) function'''


a=int(input("Enter Value Of first number:="))
b=int(input("Enter Value of second number:="))

ans=lambda a,b : max(a,b)

print("maximum value is:=",ans(a,b))