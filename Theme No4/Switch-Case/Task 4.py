initial_direction = input("Введите исходное направление (С, З, Ю, В): ").upper()
command = int(input("Введите команду (0, 1, -1): "))

directions = ["С", "В", "Ю", "З"]
index = directions.index(initial_direction)

if command == 0:
    new_direction = directions[index]
elif command == 1:
    new_direction = directions[index - 1]
elif command == -1:
    new_direction = directions[(index + 1) % 4]
else:
    new_direction = "ошибка"

print("Новое направление:", new_direction)
