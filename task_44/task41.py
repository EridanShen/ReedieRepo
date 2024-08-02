def оценка_по_числу():
    K = int(input("Введите число K (1-5): "))
    match K:
        case 1:
            print("плохо")
        case 2:
            print("неудовлетворительно")
        case 3:
            print("удовлетворительно")
        case 4:
            print("хорошо")
        case 5:
            print("отлично")
        case _:
            print("ошибка")


