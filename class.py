class Employee:
    def __init__(self, emp_name, emp_id, designation, salary):
        print("Object is created")
        self.emp_name = emp_name
        self.emp_id = emp_id
        self.designation = designation
        self.salary = salary

        print(f"Employee Created: {self.emp_name}, ID: {self.emp_id}, {self.designation}, Salary: {self.salary}")

name = input("Enter employee name: ")
emp_id = int(input("Enter employee ID: "))
designation = input("Enter designation: ")
salary =int((input("Enter salary: ")))
e1 = Employee(name, emp_id, designation, salary)
