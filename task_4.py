class EmployeeSalary:
    hourly_payment = 400
    def __init__(self,name,rest_days = None,hours = None,email = None):
        self.name = name
        self.rest_days = rest_days
        self.hours = hours
        self.email = email

    @classmethod
    def get_hours(cls,name,rest_days,hours = None,email = None):
        if hours is None:
            hours = (7 - rest_days) * 8
        return cls(name,rest_days,hours,email)
    
    @classmethod
    def get_email(cls,name,rest_days,hours,email=None):
        if email is None:
            email = f"{name}@email.com"
        return cls(name,rest_days,hours,email)
    
    @classmethod
    def set_hourly_payment(cls, hour_payment):
        cls.hourly_payment = hour_payment
        
    def salary(self):
        return self.hours * self.hourly_payment
        
    
emp1 = EmployeeSalary.get_hours("Aleksey",2)
emp2 = EmployeeSalary.get_email("Anastasiya",1,40)
print(f"Employee 1.1: {emp1.name}, Hours: {emp1.hours}, Email: {emp1.email}, Salary: {emp1.salary()}")
print(f"Employee 2.1: {emp2.name}, Hours: {emp2.hours}, Email: {emp2.email}, Salary: {emp2.salary()}")
EmployeeSalary.set_hourly_payment(500)
print(f"Employee 1.2: {emp1.name}, Hours: {emp1.hours}, Email: {emp1.email}, Salary: {emp1.salary()}")
print(f"Employee 2.2: {emp2.name}, Hours: {emp2.hours}, Email: {emp2.email}, Salary: {emp2.salary()}")

emp3 = EmployeeSalary("Sergei", 1, 35,  "sergei@yandex.ru")
print(f"Employee 3: {emp3.name}, Hours: {emp3.hours}, Email: {emp3.email}, Salary: {emp3.salary()}")    


