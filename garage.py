#import din fisierul car.py clasa Car
from car import Car

Car(1, 2, 3, 4, 5)

class Dealership:  #numele clasei incepe cu litera mare

    def __init__(self, name, address, capital, sells_make):
        self.name = name
        self.address = address
        self.capital = capital
        self.sells_make = sells_make
        self.cars = [] #initializam cars cu o lista goala

    #metoda pt a putea masinile disponibile
    def describe(self):
        print('*' * 20, f'{self.name}', '*'*20)
        print(f'{self.address}\n{self.capital} RON')
        for car in self.cars:
            if car.is_available:
                car.describe()

    #metoda pt masinile vandute
    def report(self):
        for car in self.cars:
            if not car.is_available:
                car.describe()

    #metoda prin care sa bagam o masina in dealership

def add_car(self,vin, model, buy_price):
    selling_price = buy_price * 1.5
    c = Car(vin, self.sells_make, model, selling_price)
    self.cars.append(c)
    self.capital -= buy_price

def sell_car(self, vin, discount=0):
    for car in self.cars:
        if car.vin == vin:
            if car.is_available:
                car.sell(discount)
                self.capital += car.selling_price
            else:
                print('The car is not available.')
            return #sau break, deoarece oricum nu mai avem nimic dupa for
    else:
        # nobrake
        print('Car not found.')

autoworld = Dealership('Autoworld', 'Cluj', 100000, 'VW')
autoworld.describe()

autoworld.add_car(1,'Polo', 8000)
autoworld.describe()
autoworld.add_cars(2,'Golf', 12000)
autoworld.add_cars(3,'Passat',9500)
autoworld.describe()
print()

autoworld.sell_car(2, 5) #vindem Golful cu 5% discount
autoworld.add_car(4, 'eUp', 180000)
autoworld.sell_car(3)
autoworld.describe()
autoworld.report()