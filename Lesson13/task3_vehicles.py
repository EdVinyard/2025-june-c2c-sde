class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def __str__(self):
        return f'{self.year} {self.make} {self.model}'

class Truck(Vehicle):
    def __init__(self, make, model, year, bed_capacity_lbs):
        super().__init__(make, model, year)
        self.bed_capacity_lbs = bed_capacity_lbs

class Car(Vehicle):
    def __init__(self, make, model, year, is_hatchback):
        super().__init__(make, model, year)
        self.is_hatchback = is_hatchback

vehicles = []
vehicles.append(Truck('Ford', 'Ranger', 2003, 1260.0))
vehicles.append(Car('Subaru', 'Outback', 2019, True))
vehicles.append(Car('Toyota', 'Camry', 2015, False))
for v in vehicles:
    print(v)
