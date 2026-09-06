class Employee:
 
    lang = "python" #class attributes
    salary = 12000
    
krish = Employee()
krish.name = "krish" # class instance
print(krish.name , krish.lang , krish.salary)

rohan = Employee
rohan.name = "rohan"
print(rohan.name , rohan.lang , rohan.salary)
    