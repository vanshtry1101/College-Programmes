class student:
    def getdata(self):
        self.rn = int(input("Enter roll number: "))
        self.name = input("Enter name: ")
        self.sports = input("Enter sports name: ")

    def display(self):
        print("Roll number: ", self.rn)
        print("Name: ", self.name)
        print("Sports: ", self.sports)


class subject(student):
    def getmarks(self):
        self.m1 = int(input("Enter marks1: "))
        self.m2 = int(input("Enter marks2: "))

    def putmarks(self):
        print("Marks1: ", self.m1)
        print("Marks2: ", self.m2)


class sports(student):
    def getsports(self):
        self.sport_marks = int(input("Enter sports marks: "))

    def putsports(self):
        print("Sports Marks: ", self.sport_marks)



class result(subject, sports):
    def findresult(self):
        self.total = self.m1 + self.m2 + self.sport_marks
        print("Total: ", self.total)
        self.average = self.total / 3
        print("Average: ", self.average)



r = result()
r.getdata()       
r.getmarks()      
r.getsports()     
r.display()       
r.putmarks()      
r.putsports()     
r.findresult()

   