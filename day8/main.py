class Microwave:
    def __init__(self, brand, power_rating, year):
        self.brand = brand
        self.power_rating = power_rating
        self.year = year
        self.turned_on = False

    def turnedd_on(self):
        if self.turned_on:
            print(f"Microwave {self.brand} is already turned on ")
        else:
            self.turned_on = True
            print(f"Mircowave {self.brand} is now turned on")


    def turnedd_off(self):
        if self.turned_on:
            self.turned_on = False
            print(f"Microwave {self.brand} is now turned off")
        else:
            self.turned_on = False
            print(f"Mircowave {self.brand} is already turned off")

    def run(self, seconds: int):
        if self.turned_on:
            print(f"Microwave {self.brand} is up for {seconds} seconds")
        else:
            print("Turn on ur Microwave")

smeg = Microwave("Smeg", "B", 1968)
bosch = Microwave("bosch", "A", 1912)
print(smeg.year)
print(bosch.year)
smeg.turnedd_on()
smeg.run(40)
smeg.turnedd_off()
smeg.run(10)
