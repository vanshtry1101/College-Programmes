while(1):
    print("\n*******************")
    print("Press 1 for area of square")
    print("Press 2 for area of rectangle")
    print("Press 3 for area of circle")
    print("Press 4 for area of triangle")
    print("Press 6 for exit")
    ch=int(input("what is your choice"))

    if(ch==1):
        l=float(input("Enter l="))
        area=l*l
        print("area of square=",area)

    elif(ch==2):
        l=float(input("Enter l="))
        b=float(input("Enter b="))
        area=l*b
        print("area of rectangle=",area)

    
    elif(ch==3):
        r=float(input("Enter r="))
        area=3.14*r*r
        print("area of circle=",area)

    
    elif(ch==4):
        l=float(input("Enter l="))
        h=float(input("Enter h="))
        area=1/2*l*h
        print("area of triangle=",area)
    elif(ch==5):
        break
    else:
        print("Invalid Choice")

        
