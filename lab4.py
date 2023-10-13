class Traveller:
    def __init__(self):
        self.years_to_visit = set()


    def travel(self):
        w = TimeTravel()
        if not self.years_to_visit:
            raise Exception("Додайте рік для відвідування")
        else:
            for year in self.years_to_visit:
                event = w.time_dict[year]
                print(f"Ви відвідали {year} і побачили {event}")

    def add_visit_list(self):
        w = TimeTravel()
        year = int(input("Введіть рік який ви хочете відвідати: "))
        if year in w.time_dict.keys():  
            if year in self.years_to_visit:
                raise Exception("Такий рік уже існує в множині.")
            else:
                self.years_to_visit.add(year)
        else:
            raise Exception("Такого року не існує в словнику.")

class TimeTravel:
    def __init__(self):
        self.events_list = [(1776, "Декларація незалежності США"),
               (1969, "Посадка на Місяць"),
               (1492, "Відкриття Америки"),
               (1945, "Завершення Другої світової війни")]
        self.time_dict = {year: event for year, event in self.events_list}

    def add_event(self):
        t = Traveller()
        year = int(input("Введіть рік події: "))
        event_description = input("Введіть опис події: ")
        
        if year in t.years_to_visit:
            raise Exception(f"Подія для року {year} вже існує у списку подій.")
        else:
            self.time_dict[year] = event_description
            self.events_list.append((year, event_description))
            print(f"Подія {event_description} у {year} була додана до словника часу.")
            print("Оновлений список подій:")
       
    def remove_event(self):
        year_to_remove = int(input("Введіть рік події для видалення: "))
        if year_to_remove in self.time_dict.keys():
            event_to_remove = self.time_dict.get(year_to_remove)
            self.events_list = [(year, event) for year, event in self.events_list if year != year_to_remove]
            del self.time_dict[year_to_remove]
            print(f"Подія {event_to_remove} у {year_to_remove} була видалена.")
        else:
            raise Exception(f"Подія для року {year_to_remove} не знайдена у списку подій.")

first_travel = Traveller()
time_travel = TimeTravel()

while True:
    for year in time_travel.time_dict:
        if year in time_travel.time_dict:
            event = time_travel.time_dict[year]
            print(f"У {year} відбулася подія: {event}")
    
    action = input("Бажаєте додати подію в словник (с), або додати подію в множину (м) або видалити (в) подію, або подорожувати (п), або завершити (з) програму? ").lower()
    
    match action:
        case 'с':
            time_travel.add_event()
        case 'м':
            first_travel.add_visit_list()
        case 'п':
            first_travel.travel()
        case 'в':
            time_travel.remove_event()
        case 'з':
            break
        case _:
            print("Невірний вибір. Спробуйте ще раз.")
        