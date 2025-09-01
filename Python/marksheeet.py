class student:
   def getdata(self):
      self.name=input("Enter Name:")
      self.rn=int(input("Enter No:"))
      self.sub1=int(input("Enter Sub1:"))
      self.sub2=int(input("Enter Sub2:"))
      self.sub3=int(input("Enter Sub3:"))

   def findresult(self):
      self.total=self.sub1+self.sub2+self.sub3
      self.avg=self.total/3

      if(self.sub1>=40 and self.sub2>=40 and self.sub3>=40):
         if(self.avg>=80):
            self.grade="A"
         elif(self.avg>=60): 
            self.grade="B"     
         elif(self.avg>=40): 
            self.grade="C"
         elif(self.avg<=40): 
            self.grade="Fail"

   def display(self):
      print("Roll NO:=",self.rn)
      print("Name Is:=",self.name)
      print("Subject 1=",self.sub1)
      print("Subject 2=",self.sub2)
      print("Subject 3:=",self.sub3)                 
      print("Total Is:=",self.total)
      print("Avg IS:=",self.avg)
      print("Grade Is:=",self.grade)



s=student()
s.getdata()
s.findresult()
s.display()      