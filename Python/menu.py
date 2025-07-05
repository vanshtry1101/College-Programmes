while(1):
    print("Enter 1 for prime Number")
    print("Enter 2 to check given number is even or odd")
    print("Enter 3 for check number is positive using ASSERT")
    n=int(input("Enter Your Choice:="))
    ch=n 

    if(ch==1):
     s=int(input("Give The Number:="))
     for i in range(2,s):
        if(s%i==0):
         print("Not Prime Number")
        else:
         print("Prime Number")
         break
    if(ch==2):
        i=int(input("Give The Number:="))
        if(i%2==0): 
            print("Number Is Even")
        else:   
            print("Number Is Odd")
    if(ch==3):
       n=int(input("Enter No:="))
       assert n>0
       print("No Is Positive")       

