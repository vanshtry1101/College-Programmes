# ex of mro function 

# in python every class is subclass or superclass of object class 
# the object class is the topmost class in python
# every class is subclass of object class directly or indirectly
# search the order in which the methods are resolved is called method resolution order(mro)
# depth first left to right approach is used to find the method in mro
# no searching in the same class more than once
class A:
        def display(self):
                print("I am a class A")
class B(A):
        def display(self):
                print("I am a class B")

class C(A):
        def display(self):
                print("I am a class C")
class D(B,C):
        def display(self):
                print("I am a class D")

print(D.__mro__)