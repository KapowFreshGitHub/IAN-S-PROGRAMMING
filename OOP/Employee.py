class Employee:
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "" + last + "@gmail.com"

    def fullname(self):
        return self.first, self.last

emp_1 = Employee("Nicole", "Carrera", 1000000)
emp_2 = Employee("Debbie", "Carrera", 1000005)

print(emp_1.email)
print(emp_2.email)

print(emp_1.fullname())
#print(emp_1.email, emp_2.email)

