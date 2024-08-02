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
