class Student():
    def set_details(self, name, sid, branch, perc, age, year, certs):
        self.name = name
        self.sid = sid
        self.branch = branch
        self.perc = perc
        self.age = age
        self.year = year
        self.certs = certs
    def get_details(self):
        print(f"{self.name}, {self.sid}, {self.branch}, {self.perc}%, {self.age} yrs, PassOut: {self.year}, Certs: {self.certs}")
students = []
for i in range(10):
    s = Student()
    s.set_details(f"Stu{i+1}", f"S10{i+1}", "CSE" if i % 2 == 0 else "ECE", 70 + i, 20 + i % 3, 2025 + i % 2, i + 1)
    students.append(s)
for s in students:
    s.get_details()