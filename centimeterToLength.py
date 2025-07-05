cm = float(input("Enter Centimeter: "))

if (cm < 0):
    print("Invalid Input")
else:
    inch = cm / 2.54
    print("Cm =", cm)
    print("Inch =", inch)
