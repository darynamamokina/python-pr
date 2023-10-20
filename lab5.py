class Parsable:
    def init(self, path="text.txt") -> None:
        self.path = path

    def parse(self, content=None, sep=","):
        raise NotImplementedError

class Headerable:
    def get_header(self):
        raise NotImplementedError

class Syncable:
    def sync(self):
        raise NotImplementedError

class DataStorage:
    data = []

class FileSyncable(Syncable, DataStorage):
    def sync(self, path):
        if len(self.data) > 0:
            with open(path, '+wt') as f:
                pass

            for car in self.data:
                with open(path, "a") as f:
                    f.write(f"{car.brand},{car.model},{car.year},{car.color}\n")

        self.data = []

        with open(path, "r") as f:
            line = f.readline()
            while line:
                self.data.append(car.parse(line))
                line = f.readline()


    def display_all_cars(self):
        db_path = "database.csv"  

        with open(db_path, "r") as db_file:
            print("Список автомобілів в базі:")
            for line in db_file:
                car_data = line.strip().split(",")
                brand, model, year, color = car_data
                print(f"Марка: {brand}, Модель: {model}, Рік: {year}, Колір: {color}")


    def delete_car(self, brand):
        db_path = "database.csv" 

        with open(db_path, "r") as db_file:
            lines = db_file.readlines()

        with open(db_path, "w") as db_file:
            for line in lines:
                car_data = line.strip().split(",")
                car_brand = car_data[0]  
                if car_brand != brand:
                    db_file.write(line)

        self.data = [car for car in self.data if car.brand != brand]

class Car(Parsable, Headerable):
    def __init__(self, brand, model, year, color):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color

    def get_header(self):
        return self.dict.keys()

    def parse(self, content=None, sep=","):
        if (content is not None):
            self.brand, self.model, self.year, self.color = content.split(sep)
            return self
        return sep.join([self.brand, self.model, str(self.year), self.color])


class DB(FileSyncable):
    __instance = None

    def __init__(self) -> None:
        self.data = []

    @classmethod
    def get_instance(cls):
        if cls.__instance is None:
            cls.__instance = DB()
        return cls.__instance

    def add_car(self, car):
        self.data.append(car)

    def sync(self, path="database.csv"):
        return super().sync(path)
    
    def add_car_manually(self):
        brand = input("Введіть марку автомобіля: ")
        model = input("Введіть модель автомобіля: ")
        year = int(input("Введіть рік випуску автомобіля: "))
        color = input("Введіть колір автомобіля: ")

        car = Car(brand, model, year, color)
        self.data.append(car)

if __name__ == "__main__":
    db = DB.get_instance()

    while True:
        add_more = input("Бажаєте додати (д) автомобіль у базу, видалити (в) чи переглянути (п) автомобілі?").lower()
        match add_more:
            case 'д':
                db.add_car_manually()
            case 'в':
                add_brand = input("Введіть марку автомобіля, який хочете видалити: ").lower()
                db.delete_car(add_brand)
            case 'п':
                break
            case _:
                print("Невірний вибір. Спробуйте ще раз.")
        

db.sync()
db.display_all_cars()
    
for car in db.data:
    print(car.brand)