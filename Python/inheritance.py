# Polymorphism := more than one form in enharitance
# there are 4 types of polymorphism in python

###################################################################################################################################

# 1. Method Overriding (in heritance if the child class has the same method as the parent class then the method of the child class is called method overriding) 
class A:
    def display(self):
        print("Class A method")

class B(A):
    def display(self):
        super().display()
        print("Class B method")

t=B()
t.display()

###################################################################################################################################

# 2. Method Overloading in inheritance parent and child class have the same method name but argument must be different
class C:
    def display(self):
        print("Class C method with no argument")

class D(C):
    def display(self,x):
        super().display()
        print("Class D method with one argument:",x)
t=D()
t.display(5)            

###################################################################################################################################

# default constructor in inheritance
class E:
    def __init__(self,x):
        print("Class E default constructor",x)
class F(E):
    def __init__(self,x):
        super().__init__(x)
        print("Class F default constructor")

t=F(10)  # it will not call the parent constructor
# to call the parent constructor we use super()

###################################################################################################################################

# 3. Operator Overloading (dunder method)


# 4. Duck Typing


        
