def is_positive(A):
    return A > 0

def is_odd(A):
    return A % 2 != 0

def is_even(A):
    return A % 2 == 0

def inequalities_A_gt_2_and_B_le_3(A, B):
    return A > 2 and B <= 3

def inequalities_A_ge_0_or_B_lt_minus_2(A, B):
    return A >= 0 or B < -2

def double_inequality_A_lt_B_lt_C(A, B, C):
    return A < B < C

def B_between_A_and_C(A, B, C):
    return A < B < C or C < B < A

def both_A_and_B_odd(A, B):
    return A % 2 != 0 and B % 2 != 0

def at_least_one_odd(A, B):
    return A % 2 != 0 or B % 2 != 0

def exactly_one_odd(A, B):
    return (A % 2 != 0) != (B % 2 != 0)

# Примеры использования
A = int(input("Введите целое число A: "))
print("Число A является положительным:", is_positive(A))

A = int(input("Введите целое число A: "))
print("Число A является нечетным:", is_odd(A))

A = int(input("Введите целое число A: "))
print("Число A является четным:", is_even(A))

A = int(input("Введите целое число A: "))
B = int(input("Введите целое число B: "))
print("Справедливы неравенства A > 2 и B ≤ 3:", inequalities_A_gt_2_and_B_le_3(A, B))

A = int(input("Введите целое число A: "))
B = int(input("Введите целое число B: "))
print("Справедливы неравенства A ≥ 0 или B < -2:", inequalities_A_ge_0_or_B_lt_minus_2(A, B))

A = int(input("Введите целое число A: "))
B = int(input("Введите целое число B: "))
C = int(input("Введите целое число C: "))
print("Справедливо двойное неравенство A < B < C:", double_inequality_A_lt_B_lt_C(A, B, C))

A = int(input("Введите целое число A: "))
B = int(input("Введите целое число B: "))
C = int(input("Введите целое число C: "))
print("Число B находится между числами A и C:", B_between_A_and_C(A, B, C))

A = int(input("Введите целое число A: "))
B = int(input("Введите целое число B: "))
print("Каждое из чисел A и B нечетное:", both_A_and_B_odd(A, B))

A = int(input("Введите целое число A: "))
B = int(input("Введите целое число B: "))
print("Хотя бы одно из чисел A и B нечетное:", at_least_one_odd(A, B))

A = int(input("Введите целое число A: "))
B = int(input("Введите целое число B: "))
print("Ровно одно из чисел A и B нечетное:", exactly_one_odd(A, B))
