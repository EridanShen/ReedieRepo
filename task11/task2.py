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

