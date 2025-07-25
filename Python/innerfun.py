'''wap to increase value by 3 using function decorator'''
'''two functions in same programme'''

def outer(n):
    def inner(n):
        return n+3
    ans=inner(n)
    print(ans)

n=int(input("Enter No="))    
outer(n)