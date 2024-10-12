class Employee:
    company = "ITC"
    def show(self):
        print(f"The name is {self.name} and the salary is {self.salary}")

    class Programmer(Employee):
        company = "ITC Infotech"
        def show(self):
            print(f"The name is {self.langauage} and the salary is {self.salary}")


        def showLanguage(self):
            print(f"The name is {self.company} and he is good with {self.langauge} langauage")


        a = Employee()
        b = Programmer()

        print(a.company, b.company)