while(1):
    print("\n*************************")
    print("press 1 for cm to inch")
    print("press 2 for fa to cel")
    print("press 3 for farhrenit")
    print("press 4 for exit")
    ch=int(input("what your choice"))

    if(ch==1):
        i=float(input("Enter cm="))
        m=i/2.54
        print("cm to inch=",m)
    elif(ch==2):
        c=float(input("Enter celsius="))
        f=(9/5)*(c-32)
        print("fahrenhit",f)
    elif(ch==3):
        s=int(input("Enter second="))
        h=s//3600
        m=(s-(h*3600))//60
        s=(s-ch*3600)%60
        print(h)
        print(m)
        print(s)
    elif(ch==4):
        break
    else:
        print("Invaild input")
