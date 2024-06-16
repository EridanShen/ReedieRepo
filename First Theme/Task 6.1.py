def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        mid_val = arr[mid]

        if mid_val == target:
            return mid
        elif mid_val < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1  # Если элемент не найден

# Пример использования
sorted_array = [1, 3, 5, 7, 9, 11, 13, 15]
target_value = 7
index = binary_search(sorted_array, target_value)
print(f'Элемент {target_value} находится на индексе {index}')
