first_number = int(input("Введите первое число: "))
second_number = int(input("Введите второе число: "))
third_number = int(input("Введите третье число: "))

positive_count = sum(1 for x in [first_number, second_number, third_number] if x > 0)
print("Количество положительных чисел:", positive_count)
