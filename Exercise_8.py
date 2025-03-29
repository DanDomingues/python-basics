#Ex 8.1
class Vehicle:
    def __init__(self, brand:str, model:str):
        self.brand = brand
        self.model = model

    def __str__(self):
        return f"{self.brand} {self.model}"

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, value):
        self.__brand = value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        self.__model = value

#Ex 8.2
class Car(Vehicle):
    def __init__(self, brand:str, model:str, doors:int):
        super().__init__(brand, model)
        self.doors = doors

    def __str__(self):
        return f"{super().__str__()} ({self.doors} doors)"

    @property
    def doors(self):
        return self.__doors

    @doors.setter
    def doors(self, value):
        self.__doors = value

#Ex 8.3
print(Car("Honda Civic", "1975", 4))