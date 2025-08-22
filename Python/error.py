# this is an example of handling multiple errors
try:
    a = int(input("Enter Value Of 1:="))
    b = int(input("Enter Value Of 2:="))
    c = a / b
except ZeroDivisionError:
    print("Error: Divide By Zero")
except ValueError:
    print("Error: Invalid Input. Please enter integers only.")
except NameError:
    print("error:value not proper")    
else:
    print(f"Result: {c}")



