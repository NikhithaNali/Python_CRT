class Employee():
    def __init__(self,empname,empID,designation,salary,deptname):
         self.Empname=empname
         self.EmpID=empID
         self.Designation=designation
         self.salary=salary
         self.Deptname=deptname
    def Get_details(self):
        print(self.Empname)
        print(self.EmpID)
        print(self.Designation)
        print(self.salary)
        print(self.Deptname)
E1=Employee("Scott","EMP01","Data Analyst","25000","Development team")
E1.Get_details()