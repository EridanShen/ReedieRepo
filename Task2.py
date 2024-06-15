def full_meters(L):
    return L // 100

def full_tons(M):
    return M // 1000

def full_kilobytes(size_in_bytes):
    return size_in_bytes // 1024

def max_segments(A, B):
    if A <= 0 or B <= 0:
        raise ValueError("Both A and B must be positive")
    return A // B

def remaining_length(A, B):
    if A <= 0 or B <= 0:
        raise ValueError("Both A and B must be positive")
    return A % B

def left_and_right_digits(number):
    if not 10 <= number <= 99:
        raise ValueError("The number must be a two-digit number")
    left_digit = number // 10
    right_digit = number % 10
    return left_digit, right_digit

def sum_and_product_of_digits(number):
    if not 10 <= number <= 99:
        raise ValueError("The number must be a two-digit number")
    left_digit = number // 10
    right_digit = number % 10
    return left_digit + right_digit, left_digit * right_digit

def reversed_digits(number):
    if not 10 <= number <= 99:
        raise ValueError("The number must be a two-digit number")
    left_digit = number // 10
    right_digit = number % 10
    return right_digit * 10 + left_digit

def first_digit_of_three_digit(number):
    if not 100 <= number <= 999:
        raise ValueError("The number must be a three-digit number")
    return number // 100

def last_and_middle_digits(number):
    if not 100 <= number <= 999:
        raise ValueError("The number must be a three-digit number")
    last_digit = number % 10
    middle_digit = (number // 10) % 10
    return last_digit, middle_digit

# Примеры использования
L = int(input("Введите расстояние в сантиметрах: "))
print("Количество полных метров:", full_meters(L))

M = int(input("Введите массу в килограммах: "))
print("Количество полных тонн:", full_tons(M))

size_in_bytes = int(input("Введите размер файла в байтах: "))
print("Количество полных килобайтов:", full_kilobytes(size_in_bytes))

A = int(input("Введите длину отрезка A: "))
B = int(input("Введите длину отрезка B: "))
print("Количество отрезков B на отрезке A:", max_segments(A, B))
print("Длина незанятой части отрезка A:", remaining_length(A, B))

number = int(input("Введите двузначное число: "))
left_digit, right_digit = left_and_right_digits(number)
print("Левая цифра:", left_digit)
print("Правая цифра:", right_digit)
sum_digits, prod_digits = sum_and_product_of_digits(number)
print("Сумма цифр:", sum_digits)
print("Произведение цифр:", prod_digits)
print("Число при перестановке цифр:", reversed_digits(number))

three_digit_number = int(input("Введите трехзначное число: "))
print("Первая цифра трехзначного числа:", first_digit_of_three_digit(three_digit_number))
last_digit, middle_digit = last_and_middle_digits(three_digit_number)
print("Последняя цифра трехзначного числа:", last_digit)
print("Средняя цифра трехзначного числа:", middle_digit)
