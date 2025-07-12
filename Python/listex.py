l1=[11,20,34,50,67]
l2=[24,56,78,89,45]

l3=l1+l2   
print(l3)  #[11, 20, 34, 50, 67, 24, 56, 78, 89, 45]

print(34 in l1)    #true
print(36 not in l1)  #false
print(l1*2)    #[11, 20, 34, 50, 67, 11, 20, 34, 50, 67]
print(2*l1)    #[11, 20, 34, 50, 67, 11, 20, 34, 50, 67]

print(min(l1))  #11
print(max(l1))  #67
print(l2.count(90))

#l1.append(l2)
#print(l1)  #[11, 20, 34, 50, 67, [24, 56, 78, 89, 45]]

l1.extend(l2)
print(l1)  #[11, 20, 34, 50, 67, 24, 56, 78, 89, 45]


'''-----------------------------------------------------------'''


print(l1.index(36))

print(l1[1:4])

del l1[2]
print(l1)

del l1[3:5]
print(l1)

l1[2:4]=[45,"hello",6.7]
print(l1)

l1=l2
print(l1)

l1.insert(3,100)
print(l1)

l1.sort()
print(l1)

l1.pop(4)
print(l1)

l1.remove(11)
print(l1)

l1.clear()
print(l1)