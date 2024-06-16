def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Устанавливаем флаг для проверки, был ли совершен обмен
        swapped = False
        # Последние i элементов уже отсортированы
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Меняем элементы местами
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # Если не было обменов, массив уже отсортирован
        if not swapped:
            break

# Пример использования
unsorted_array = [64, 34, 25, 12, 22, 11, 90]
print(f'Несортированный массив: {unsorted_array}')
bubble_sort(unsorted_array)
print(f'Отсортированный массив: {unsorted_array}')
