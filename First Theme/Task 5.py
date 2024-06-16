person = {
    "имя": "Джонни",
    "возраст": 27,
    "пол": "мужской",
    "рост": 173,
    "вес": 60
}

print("Данные о человеке:")
for key, value in person.items():
    print(f"{key.capitalize()}: {value}")

person["размер ноги"] = 43
print("\nПосле добавления размера ноги:")
for key, value in person.items():
    print(f"{key.capitalize()}: {value}")

del person["возраст"]
print("\nПосле удаления возраста:")
for key, value in person.items():
    print(f"{key.capitalize()}: {value}")
