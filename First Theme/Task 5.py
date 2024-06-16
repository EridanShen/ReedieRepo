# Создаем словарь с данными о человеке
person = {
    "имя": "Джонни",
    "возраст": 27,
    "пол": "мужской",
    "рост": 173,
    "вес": 60
}

# Выводим на экран все данные о человеке по ключам
print("Данные о человеке:")
for key, value in person.items():
    print(f"{key.capitalize()}: {value}")

# Добавляем в словарь ключ и значение размера ноги
person["размер ноги"] = 43
print("\nПосле добавления размера ноги:")
for key, value in person.items():
    print(f"{key.capitalize()}: {value}")

# Удаляем из словаря возраст
del person["возраст"]
print("\nПосле удаления возраста:")
for key, value in person.items():
    print(f"{key.capitalize()}: {value}")
