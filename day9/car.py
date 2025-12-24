class Car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def info(self):
        print(f"Brand: {self.brand}. Year: {self.year}")

    def is_old(self):
        if self.year < 2025:
            print("Car is old.")
        else:
            print("Good to go!")

car1 = Car("Honda", 1920)
car2 = Car("Monza", 2026)

car1.info()
car2.info()

car1.is_old()
car2.is_old()
