'''default argument'''


def interest(p=500,r=0.10,n=1):
    print("interest amount=",p*r*n)

interest()    
interest(2000,5)
interest(5000,3,1)



############################################

# def amount(p=500,r=0.10,n=1):
#     ans=p*r*n
#     print(ans)

# amount()
# amount(10000)    
