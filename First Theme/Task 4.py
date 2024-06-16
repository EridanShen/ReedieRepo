# Часть 1: Индексирование и срезы
list1 = [1, 2, 3, 4, 5]
print("Первый элемент:", list1[0])
print("Третий элемент:", list1[2])
print("Срез из первых трех элементов:", list1[:3])

# Часть 2: Исправление элемента в списке
city_list = ["Ростов", "+", "на", "-", "Дону"]
city_list[1] = "-"
city_name = city_list[0] + city_list[1] + city_list[2] + city_list[3] + city_list[4]
print("Название города:", city_name)

# Часть 3: Разделение списка на буквы и числа
mixed_list = ["a", "s", "1", "a", "32", "23"]
letters = [x for x in mixed_list if x.isalpha()]
numbers = [x for x in mixed_list if x.isdigit()]
print("Список с буквами:", letters)
print("Список с числами:", numbers)

# Часть 4: Удаление последнего элемента и реверсия списка
if letters:
    letters.pop()
letters.reverse()
print("Список с буквами после удаления последнего элемента и реверсии:", letters)

# Часть 5: Преобразование списка в множество
mixed_set = set(mixed_list)
print("Множество из списка:", mixed_set)
print("Изменения: дубликаты были удалены, и порядок элементов в множестве не гарантируется.")
