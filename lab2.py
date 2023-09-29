import random

class Animal:
    def __init__(self, age, quality, mass):
        self._age = age
        self._quality = quality
        self._mass = mass

    def produce_milk(self):
        return 0  # Молоко виробляють коровами

    def lay_eggs(self):
        return 0  # Яйця несуть кури

    def prepare_land(self):
        return 0  # Свині не допомагають організовувати землю

    def butcher(self):
        return self._mass * self._quality  # М'ясо, яке можна отримати з тварини

class Cow(Animal):
    def __init__(self, age, quality, mass, price):
        super().__init__(age, quality, mass)
        self._price = price

    def produce_milk(self):
        return self._mass * self._quality * 0.1  # Корови виробляють молоко

    def reproduce(self):
        reproduction_chance = 0.1
        if random.random() < reproduction_chance:
            new_cow = Cow(age=0, quality=self._quality, mass=50, price=self._price)  # Нова корова має невеликий масив
            return new_cow
        return None

class Chicken(Animal):
    def __init__(self, age, quality, mass, price):
        super().__init__(age, quality, mass)
        self._price = price

    def lay_eggs(self):
        return self._mass * self._quality * 0.05  # Кури несуть яйця

    def reproduce(self):
        reproduction_chance = 0.2
        if random.random() < reproduction_chance:
            new_chicken = Chicken(age=0, quality=self._quality, mass=0.5, price=self._price)
            return new_chicken
        return None

class Pig(Animal):
    def __init__(self, age, quality, mass, price):
        super().__init__(age, quality, mass)
        self._price = price

    def prepare_land(self):
        return self._mass * self._quality * 0.2  # Свині допомагають організовувати землю

    def reproduce(self):
        reproduction_chance = 0.15
        if random.random() < reproduction_chance:
            new_pig = Pig(age=0, quality=self._quality, mass=10, price=self._price)  # Нова свиня має невеликий масив
            return new_pig
        return None

class Selling:
    def __init__(self, product, quantity):
        self._product = product
        self._quantity = quantity

    def get_product_name(self):
        return self._product.__class__.__name__

    def get_quantity(self):
        return self._quantity

    def get_total_price(self):
        return self._product._price * self._quantity  # Отримана сума за продаж продукту

class Farm:
    def __init__(self):
        self._animals = []
        self._sellings = []
        self._balance = 0

        # Додавання початкової кількості тварин
        for _ in range(5):
            cow = Cow(age=random.randint(1, 10), quality=random.uniform(0.7, 0.9), mass=random.randint(300, 700), price=1000)
            self._animals.append(cow)
        for _ in range(10):
            chicken = Chicken(age=random.randint(1, 5), quality=random.uniform(0.6, 1.0), mass=random.uniform(1.5, 3.0), price=50)
            self._animals.append(chicken)
        for _ in range(5):
            pig = Pig(age=random.randint(1, 8), quality=random.uniform(0.5, 0.8), mass=random.randint(150, 300), price=800)
            self._animals.append(pig)

    def add_animal(self, animal):
        self._animals.append(animal)

    def display_summary(self):
        cow_count = sum(isinstance(animal, Cow) for animal in self._animals)
        chicken_count = sum(isinstance(animal, Chicken) for animal in self._animals)
        pig_count = sum(isinstance(animal, Pig) for animal in self._animals)

        print(f"Загальна кількість тварин:")
        print(f"Корів: {cow_count}")
        print(f"Курей: {chicken_count}")
        print(f"Свиней: {pig_count}")

    def display_full_list(self, animal_type):
        filtered_animals = [animal for animal in self._animals if isinstance(animal, animal_type)]

        if not filtered_animals:
            print(f"На фермі немає {animal_type.__name__}")
            return



    def sell(self, animal_type, max_quantity):
        animals_to_sell = [animal for animal in self._animals if isinstance(animal, animal_type)]

        if not animals_to_sell:
            print(f"На фермі немає {animal_type.__name__}")
            return

        quantity_to_sell = random.randint(1, min(max_quantity, len(animals_to_sell)))
        total_price = 0

        # Видаляємо партію тварин
        animals_to_remove = random.sample(animals_to_sell, quantity_to_sell)
        for animal in animals_to_remove:
            total_price += animal._price
            self._animals.remove(animal)

        selling = Selling(animal_type(0, 0, 0, 0), quantity_to_sell)
        self._sellings.append(selling)
        self._balance += total_price

        print(f"Продано {quantity_to_sell} одиниць {animal_type.__name__}")
        print(f"Загальна сума: {total_price} грн")

    def hatch_chicken(self, chicken):
        hatch_chance = 0.2
        if random.random() < hatch_chance:
            new_chicken = Chicken(age=0, quality=random.uniform(0.6, 1.0), mass=0.5, price=100)
            self.add_animal(new_chicken)

    def reproduce_animals(self):
        new_animals = []
        for animal in self._animals:
            if isinstance(animal, (Cow, Pig)):
                new_animal = animal.reproduce()
                if new_animal:
                    new_animals.append(new_animal)
        self._animals.extend(new_animals)

    def kill_animal(self, animal):
        if animal in self._animals:
            self._animals.remove(animal)

    def check_age(self):
        for animal in self._animals:
            if animal._age >= 4:
                self.kill_animal(animal)

    def get_balance(self):
        return self._balance

    def get_animal_count(self):
        return len(self._animals)

# Створення ферми
farm = Farm()

print(f"Баланс ферми: {farm.get_balance()} грн")

# Продаж продуктів та підрахунок балансу
farm.sell(Cow, 5)  # Продаж корів (від 1 до 5)
farm.sell(Chicken, 10)  # Продаж курей (від 1 до 10)
farm.sell(Pig, 5)  # Продаж свиней (від 1 до 5)


print(f"Баланс ферми: {farm.get_balance()} грн")

# Розмноження курей
for _ in range(10):
     farm.hatch_chicken(Chicken)


# Виконання вбивства тварин
animal_to_kill = random.choice(farm._animals)
farm.kill_animal(animal_to_kill)
print(f"{animal_to_kill.__class__.__name__} була вбита")