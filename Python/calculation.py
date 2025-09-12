import employee

basic_salary=int(input("Enter Basic Salary:="))

da=employee.calculate_DA(basic_salary)
hra=employee.calculate_HRA(basic_salary)
pf=employee.calculate_PF(basic_salary)
gross_salary=basic_salary + da + hra 
itax = employee.calculate_ITAX(gross_salary)
net_salary = gross_salary - pf - itax

print("DA is:=",da)
print("hra is:=",hra)
print("pf is:=",pf)
print("gross salary is:=",gross_salary)
print("itax is:=",itax)
print("net salary is:=",net_salary)

  

          