cpp = int(input("Enter Cpp Marks: "))
java = int(input("Enter Java Marks: "))
c = int(input("Enter C Marks: "))

print("Cpp Marks", cpp)
print("Java Marks", java)
print("C Marks:", c)

if(cpp < 33 and java < 33 and c < 33):
    print("Fail")
    exit(0)

total = cpp + java + c
avg = total / 3

print("Total Marks:", total)
print("Percentage:",avg)


if (avg >= 85):
    grade = "A"
elif (avg >= 70 and avg < 85):
    grade = "B"
elif(avg >= 55 and avg < 70):
    grade = "C"
else:
    grade = "D"

print("Grade:", grade)

