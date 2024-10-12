class Employee :
    language = "python" # This is class attribute
    salary = 1200000

    def __init__(self,name,salary,langauge):#dunder method 
        self.name = name 
        self.salary = salary 
        self.langauge = langauge
        print("I am creating is an object ")
     


    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")


    def greet(self):print("Good morning")
    

Nikita = Employee("Nikita",1300000,"Javaskript")
print(Nikita.name,Nikita.salary,Nikita.langauge)


