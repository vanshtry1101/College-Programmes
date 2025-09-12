# circle --> area , perimeter 


class Circle:
    def findarea(self):
       r=int(input("Enter the radius of circle: "))
       area=3.14*r*r
       print("Area of circle is:",area)
    def findperiemter(self):
        r=int(input("Enter the radius of circle: "))
        periemeter=2*3.14*r
        print("perimeter of circle is:",periemeter)

s=Circle()
s.findarea()
s.findperiemter()