class Employee :
    language = "python" # This is class attribute
    salary = 1200000

    def __init__(self):#dunder method 
        print("I am creating is an object ")
     


    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")


    def greet(self):print("Good morning")
    

Nikita = Employee()
Nikita.language = "Javaskript"  # This is an instant attribute

Nikita.getInfo()
Nikita.greet()