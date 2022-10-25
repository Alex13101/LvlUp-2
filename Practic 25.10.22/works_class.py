class my_car:
    def __init__(self, color, name, mileage):
        self.color = color
        self.name = name
        self.mileage = mileage

    def mileage(self):
        self.mileage += input("Сколько проехали?:  ")
        print("Машина прошла ", self.mileage())


my_car1 = my_car("red", "toyota", 0)
my_car2 = my_car("blue", "Lada", 0)

my_car1.mileage(my_car2)
