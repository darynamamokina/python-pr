# Створення списку подій з використанням кортежів
events_list = [(1776, "Декларація незалежності США"),
               (1969, "Посадка на Місяць"),
               (1492, "Відкриття Америки"),
               (1945, "Завершення Другої світової війни")]

# Створення словника часу зі списку подій
time_dict = {year: event for year, event in events_list}

# Ініціалізація множини років, які ви хочете відвідати
years_to_visit = {year for year, _ in events_list}

# Функція для додавання події в словник часу
def add_event():
    year = int(input("Введіть рік події: "))
    event_description = input("Введіть опис події: ")
    
    if year in years_to_visit:
        print(f"Подія для року {year} вже існує у списку подій.")
    else:
        time_dict[year] = event_description
        events_list.append((year, event_description))  # Додавання до списку подій
        years_to_visit.add(year)  # Оновлення множини років для відвідування
        print(f"Подія {event_description} у {year} була додана до словника часу.")
        print("Оновлений список подій:")
        

# Функція для видалення події за роком
def remove_event(events_list):
    year_to_remove = int(input("Введіть рік події для видалення: "))
    
    if year_to_remove in years_to_visit:
        event_to_remove = time_dict.get(year_to_remove)
        events_list = [(year, event) for year, event in events_list if year != year_to_remove]
        years_to_visit.remove(year_to_remove)
        del time_dict[year_to_remove]
        print(f"Подія {event_to_remove} у {year_to_remove} була видалена.")
    else:
        print(f"Подія для року {year_to_remove} не знайдена у списку подій.")


# Головний код
while True:
    for year in years_to_visit:
        if year in time_dict:
            event = time_dict[year]
            print(f"У {year} відбулася подія: {event}")
    
    action = input("Бажаєте додати (д) або видалити (в) подію, або завершити (з) програму? ").lower()
    
    if action == 'д':
        add_event()
        action = ''  # Змінити значення action на пустий рядок
    elif action == 'в':
        remove_event(events_list)  # Викликаємо функцію з передачею змінної events_list
        action = ''  # Змінити значення action на пустий рядок
    elif action == 'з':
        break
    else:
        print("Невірний вибір. Спробуйте ще раз.")




