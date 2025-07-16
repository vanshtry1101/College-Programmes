'''Wap Prog To remove repeted elements from list'''
# Don't Print The Repeated List

l=[45,67,78,90,54,45,67]
r=[]

for n in l:
 if n not in r:
  r.append(n)

print("Original (with repeat)",l)
print("Withour repeatation",r)  