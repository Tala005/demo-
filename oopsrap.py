#  1. Abstraction & Encapsulation: We define a class with only essential features
class Vehicle:
    def __init__(self, brand, model):
        self._brand = brand        # encapsulated attribute
        self._model = model

    def display_info(self):
        print(f"\t Brand: {self._brand},\n \t Model: {self._model}")

#  2. Inheritance: Car and Bike inherit from Vehicle
class Car(Vehicle):
    def __init__(self, brand, model, doors):
        super().__init__(brand, model)
        self._doors = doors

    def display_info(self):
        # 3. Polymorphism: Overriding the parent method
        print(f"Car -\t Brand: {self._brand},\n \t Model: {self._model},\n \t Doors: {self._doors}")

class Bike(Vehicle):
    def __init__(self, brand, model, engine_cc):
        super().__init__(brand, model)
        self._engine_cc = engine_cc

    def display_info(self):
        #  3. Polymorphism: Another overridden method
        print(f"Bike - \t Brand: {self._brand},\n \t Model: {self._model},\n \t Engine: {self._engine_cc}cc")

#  Creating objects (instances) → Object-oriented structure
car1 = Car("Toyota", "Corolla", 4)
bike1 = Bike("Yamaha", "R15", 150)

#  Using methods (behaviors)
car1.display_info()   # Car-specific display (polymorphism)
bike1.display_info()  # Bike-specific display (polymorphism)

