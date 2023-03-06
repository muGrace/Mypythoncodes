class Employee:
    'Common base classfor all employee'
    empCount=0
def _init_(self,name,salary):
    self.name=name
    self.salary=salary
    Employee.empCount+=1
    
def displayCount(self):
    print("Total Employee %d"% Employee.empCount)
def displayEmployee(self):

    print("Name:",self.name,",Salary:",self.salary)
    emp1=Employee("Manni",2000)
    emp2=Employee("zara",800)
    emp1=displayEmployee()
    emp2=displayEmployee()
    print("Total Employee %d"%Employee.empCount)

	

    
