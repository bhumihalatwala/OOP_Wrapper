class Employee:
    def __init__(self, name, age, emp_id=None, salary=None): 
        self.name = name
        self.age = age
        self.__emp_id = emp_id
        self.__salary = salary

    def setID(self, emp_id):
        if emp_id:
            self.__emp_id = emp_id
        else:
            print("No Employee Id provided")

    def getID(self):
        return self.__emp_id
    
    def setSalary(self, salary):
        if salary:
            self.__salary = salary
        else:
            print("No Salary provided")

    def getSalary(self):
        return self.__salary
    
    def display(self):
        print(f"Employee Details: Name: {self.name}, Age: {self.age}, ID: {self.__emp_id}, Salary: {self.__salary}")

    def __str__(self):
        return f"Employee(Name: {self.name}, Age: {self.age}, ID: {self.__emp_id}, Salary: ${self.__salary})"
    
    def __eq__(self, other):
        return self.__salary == other.__salary
    
    def __lt__(self, other):
        return self.__salary < other.__salary
    
    def __gt__(self, other):
        return self.__salary > other.__salary
    
    def __del__(self):
        print(f"Employee {self.name} resources freed.")

class Manager(Employee):
    def __init__(self, name, age, emp_id, salary, dept):
        super().__init__(name, age, emp_id, salary)
        self.dept = dept

    def display(self):
        super().display()
        print(f"Department: {self.dept}")

    def __str__(self):
        return super().__str__() + f", Department: {self.dept}"


class Developer(Employee):
    def __init__(self, name, age, emp_id, salary, lang):
        super().__init__(name, age, emp_id, salary)
        self.lang = lang

    def display(self):
        super().display()
        print(f"Programming Language: {self.lang}")
    
    def __str__(self):
        return super().__str__() + f", Programming Language: {self.lang}"
    
class Person(Employee):
    def __init__(self, name, age):
        super().__init__(name, age)
    
    def display(self):
        print(f"Person created with name: {self.name} and age: {self.age}")


Employees = {}

print("\n--- Employee Management System ---")

while True:
    print("Choose an operation: ")
    print("1. Create a Person")
    print("2. Create an Employee")
    print("3. Create a Manager")
    print("4. Show Details")
    print("5. Compare Salaries")
    print("6. Exit") 
    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        print(f"Person created with name: {name} and age: {age}.")
        print()
        print("--------Choose another operation.--------")
        print()
        
    elif choice == 2:
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        emp_id = input("Enter Employee ID: ")
        salary = float(input("Enter Salary: "))
        if emp_id in Employees:
            print("Employee ID already exists. Try again.")
            print()
            print("--------Choose another operation.--------")
            print()
        else:
            Employees[emp_id] = Employee(name, age, emp_id, salary)  
            print(f"Employee created with name: {name}, age: {age}, ID: {emp_id}, and salary: ${salary}.")
            print()
            print("--------Choose another operation.--------")
            print()

    elif choice == 3:
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        emp_id = input("Enter Employee ID: ")
        salary = float(input("Enter Salary: "))
        dept = input("Enter Department: ")
        if emp_id in Employees:
            print("Employee ID already exists. Try again.")
            print()
            print("--------Choose another operation.--------")
            print()
        else:
            Employees[emp_id] = Manager(name, age, emp_id, salary, dept)
            print(f"Manager created with name: {name}, age: {age}, ID: {emp_id}, salary: ${salary}, and department: {dept}.")
            print()
            print("--------Choose another operation.--------")
            print()

    elif choice == 4:
        if not Employees:
            print("No employees available.")
            print()
            print("--------Choose another operation.--------")
            print()
        else:
            emp_id = input("Enter Employee ID to view details: ")
            if emp_id in Employees:
                Employees[emp_id].display()
                print()
                print("--------Choose another operation.--------")
                print()
            else:
                print("Employee not found!")
                print()
                print("--------Choose another operation.--------")
                print()

    elif choice == 5:
        if len(Employees) < 2:
            print("Not enough employees to compare salaries.")
            print()
            print("--------Choose another operation.--------")
            print()
        else:
            emp_id1 = input("Enter first Employee ID: ")
            emp_id2 = input("Enter second Employee ID: ")
            
            if emp_id1 in Employees and emp_id2 in Employees:
                if Employees[emp_id1] > Employees[emp_id2]:
                    print(f"{Employees[emp_id1].name} has a higher salary than {Employees[emp_id2].name}.")
                    print()
                    print("--------Choose another operation.--------")
                    print()
                elif Employees[emp_id1] < Employees[emp_id2]:
                    print(f"{Employees[emp_id1].name} has a lower salary than {Employees[emp_id2].name}.")
                    print()
                    print("--------Choose another operation.--------")
                    print()
                else:
                    print("Both employees have the same salary.")
                    print()
                    print("--------Choose another operation.--------")
                    print()
            else:
                print("One or both employee IDs not found!")
                print()
                print("--------Choose another operation.--------")
                print()

    elif choice == 6:
        print("Exiting the system. Goodbye!")
        break
    
    else:
        print("Invalid choice. Please try again.")
