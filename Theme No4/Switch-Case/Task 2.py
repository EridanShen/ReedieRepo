def дни_в_месяце():
    месяц = int(input("Введите номер месяца (1-12): "))
    match месяц:
        case 1 | 3 | 5 | 7 | 8 | 10 | 12:
            print("31 день")
        case 4 | 6 | 9 | 11:
            print("30 дней")
        case 2:
            print("28 дней")
        case _:
            print("ошибка")

дни_в_месяце()

