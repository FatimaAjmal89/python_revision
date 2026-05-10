class Vehicle:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    def sound(self):
        print(f"vehicle makes sounds")

class Car(Vehicle):
    def __init__(self,brand,model,seats):
        super().__init__(brand,model)
        self.seats = seats

    def display1(self):
        print(f"brand = {self.brand}\n"
              f"model = {self.model}\n"
              f"seats = {self.seats}")

    def sound(self):
        print(f"car makes sounds vroom vroom")

class Bike(Vehicle):
    def __init__(self,brand,model,engine_cc):
        super().__init__(brand,model)
        self.engine_cc = engine_cc

    def display2(self):
        print(f"brand = {self.brand} \n"
              f"model = {self.model} \n"
              f"seats = {self.engine_cc}")

    def sound(self):
        print(f"bike makes sounds vroom vroom")

c1 = Car("bmw",6,4)
b1 = Bike("toyota",4,120)

c1.display1()
b1.display2()


