# hash table in Python = dictionary
razdel = input("Введите название раздела: ")
shop = {"Мясо и птица": {"Говядина", "Свинина", "Баранина", "Курица", "Индейка"},
        "Рыба": {"Лосось", "Лещ", "Карп", "Скумбрия", "Тунец", "Форель", "Сельдь"},
        "Фрукты": {"Яблоки", "Груши", "Мандарины", "Манго", "Апельсины", "Авокадо"},
        "Овощи": {"Помидоры", "Огурцы", "Капуста", "Морковь", "Картошка", "Свекла"},
        "Молочная продукция": {"Молоко", "Сыр", "Сметана", "Сливки", "Масло сливочное", "Йогурт"}}
for key, value in shop.items():
    if razdel in key:
        print(value)
        break
else:
    print("Данного раздела нет в нашем магазине")