day = int(input("Введите день: "))
month = int(input("Введите месяц: "))

days_in_month = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}

if day < days_in_month[month]:
    next_day = day + 1
    next_month = month
else:
    next_day = 1
    next_month = month + 1 if month < 12 else 1

print("Следующая дата: {}.{}".format(next_day, next_month))
