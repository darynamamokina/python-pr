import random

class Animal:
    def __init__(self, age, quality, mass):
        self.age = age
        self.quality = quality
        self.mass = mass

    def produce_milk(self):
        return 0 

    def lay_eggs(self):
        return 0 

    def prepare_land(self):
        return 0 
     
    def meat(self):
        return self.mass * self.quality  

class Cow(Animal):
    def __init__(self, age, quality, mass, price):
        super().__init__(age, quality, mass)
        self.price = price

    def produce_milk(self):
        return self.mass * self.quality * 0.1 


class Chicken(Animal):
    def __init__(self, age, quality, mass, price):
        super().__init__(age, quality, mass)
        self.price = price

    def lay_eggs(self):
        return self.mass * self.quality * 0.05 


class Pig(Animal):
    def __init__(self, age, quality, mass, price):
        super().__init__(age, quality, mass)
        self.price = price

    def prepare_land(self):
        return self.mass * self.quality * 0.2  

    
class Selling:
    def __init__(self, price, quantity):
        self.price = price
        self.quantity = quantity

class Farm:
    def __init__(self):
        self.animals = []
        self.sellings = []
        self.balance = 0

    def add_animal(self, animal):
        self.animals.append(animal)

    def list_animals(self):
        for animal in self.animals:
            print(f"{animal.__class__.__name__}: age={animal.age}, quality={animal.quality}, mass={animal.mass}")

    def sell(self, product, quantity):
        selling = Selling(product.price, quantity)
        self.sellings.append(selling)
        self.balance += product.price * quantity

    def hatch_chicken(self, chicken):
        hatch_chance = 0.2 
        if random.random() < hatch_chance:
            new_chicken = Chicken(age=0, quality=chicken.quality, mass=0.5, price=80)
            self.add_animal(new_chicken)

    def kill_animal(self, animal):
        if animal in self.animals:
            self.animals.remove(animal)

    def check_age(self):
        for animal in self.animals:
            if animal.age >= 4:
                self.kill_animal(animal)

farm = Farm()

cow = Cow(age=2, quality=0.8, mass=500, price=300)
chicken = Chicken(age=1, quality=0.9, mass=20, price=100)
pig = Pig(age=3, quality=0.7, mass=200, price=200)

farm.add_animal(cow)
farm.add_animal(chicken)
farm.add_animal(pig)

print("All animals:")
farm.list_animals()

print(f"Balance: {farm.balance} грн")


farm.sell(cow, random.randint(1, 6))
farm.sell(chicken, random.randint(1, 10))
farm.sell(pig, random.randint(1, 3))

for _ in range(10):
    farm.hatch_chicken(chicken)

print("After reproduction:")
farm.list_animals()


animal_to_kill = random.choice(farm.animals)
farm.kill_animal(animal_to_kill)
print(f"{animal_to_kill.__class__.__name__} was killed")

farm.check_age()
print("After age check:")
farm.list_animals()

print(f"Balance: {farm.balance} грн")