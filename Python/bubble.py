a=[]
n=int(input("how many number you want to enter"))

for i in range(n):
    x=int(input("enter no"))
    a.append(x)

print("Current array=",a)
n=len(a)

for i in range(n-1):
    for j in range(0,n-1):
        if a[j]>a[j+1]:
           a=[j],a[j+1]=a[j+1]
           a[j]

    print("short array=",a)