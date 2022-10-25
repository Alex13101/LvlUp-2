class my_car:
    def __init__(self, color, name, mileage):
        self.color = color
        self.name = name
        self.mileage_1 = mileage

    def mileage(self):
        n = int(input("Сколько проехали?:"))
        self.mileage_1 += n
        print(f"Машина прошла {self.name} цвета {self.color} проехала {self.mileage_1}")


my_car1 = my_car("red", "toyota", 1000)
my_car2 = my_car("blue", "Lada", 1600)
my_car3 = my_car("green", "iveco", 500)


my_car1.mileage()
my_car2.mileage()
my_car3.mileage()


