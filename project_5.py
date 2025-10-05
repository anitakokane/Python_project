print("                  Employee Management System            ")

class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print(f"Name:{self.name},age:{self.age}")

class employee(person):
    def __init__(self,name,age,empid,salary):
        super().__init__(name,age)
        self._empid=empid
        self._salary=salary
    @property
    def get_empid(self):
        return self._empid
    @get_empid.setter
    def set_empid(self,eid):
        self._empid=eid

    @property
    def get_salary(self):
        return self._salary
    @get_salary.setter
    def set_salary(self,sal):
        self._salary=sal

    def display(self):
        super().display()
        print(f"ID:{self._empid},Salary={self._salary}")
class Manager(employee):
    def __init__(self,name,age,empid,salary,department):
        super().__init__(name,age,empid,salary)
        self.department=department
    def display(self):
        super().display()
        print(f"Department:{self.department}")
people=[]
while True:
    print()
    print("1.Create a Person")
    print("2.Create an Employee")
    print("3.Create a Manager")
    print("4.show details")
    print("5.Exit")

    choice=int(input("Enter your choice:"))

    if choice==1:
        n=input("Enter Name:")
        e=int(input("Enter Age:"))
        people.append(person(n,e))
        print("Person created")
    elif choice==2:
        n=input("Enter Name:")
        e=int(input("Enter Age:"))
        eid=input("Enter Employee id:")
        sal=float(input("Enter Salary:"))
        people.append(employee(n,e,eid,sal))
        print("Employee is created")
    elif choice==3:
        n=input("Enter Name:")
        e=int(input("Enter Age:"))
        eid=input("Enter Employee id:")
        sal=float(input("Enter Salary:"))
        dep=input("Enter Department:")
        people.append(Manager(n,e,eid,sal,dep))
        print("Manager is created")
    elif choice==4:
        if len(people)==0:
            print("No records found")
        else:
            for p in people:
                p.display()
                    
    elif choice==5:
        print("Exiting the system!")
        break
    else:
        print("Enter valid choice")
    


        
                
        

            
        
        
    

