first_number = float(input("Введите первое число: "))
second_number = float(input("Введите второе число: "))
operation = input("Введите операцию (*, /, +, -): ")

if operation == "+":
    result = first_number + second_number
elif operation == "-":
    result = first_number - second_number
elif operation == "*":
    result = first_number * second_number
elif operation == "/":
    if second_number != 0:
        result = first_number / second_number
    else:
        result = "Ошибка: деление на ноль"
else:
    result = "Ошибка: неверная операция"

print("Результат:", result)
