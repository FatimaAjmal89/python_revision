from abc import ABC, abstractmethod

class Employee(ABC):

    @abstractmethod
    def salary(self):
        pass

class Intern(Employee):

    def salary(self):
        print("salary 40000")


class ContractEmployee(Employee):

    def salary(self):
        print("salary 80000")


class Fulltime(Employee):

    def salary(self):
        print("salary 100000")

I1 = Intern()
I1.salary()
C1 = ContractEmployee()
C1.salary()
F1 = Fulltime()
F1.salary()