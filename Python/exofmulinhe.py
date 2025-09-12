class student:
    def getdata(self):
        self.rn = int (input("Enter roll number: "))
        self.name = input("Enter name: ")
    def display(self):
        print("Roll number: ", self.rn)
        print("Name: ", self.name)

class getmarks(student):
    def getmarks(self):
      self.m1 = int(input("Enter marks1: "))
      self.m2 = int(input("Enter marks2: "))

    def putmarks(self):
        print("Marks1: ", self.m1)
        print("Marks2: ", self.m2)

class result(getmarks):
    def findresult(self):
        self.total = self.m1 + self.m2
        print("Total: ", self.total)
        self.average = self.total / 2
        print("Average: ", self.average)

s = result()
s.getdata()
s.getmarks()
s.display()
s.putmarks()
s.findresult() 