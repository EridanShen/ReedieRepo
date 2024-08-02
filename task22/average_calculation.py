import logging

# Настройка логирования
logging.basicConfig(filename='average_calculation.log', level=logging.INFO, format='%(asctime)s %(message)s')


def calculate_average(numbers):
    try:
        logging.info(f'Calculating average for the list: {numbers}')
        if not all(isinstance(num, (int, float)) for num in numbers):
            raise ValueError("List contains non-numeric elements.")
        avg = sum(numbers) / len(numbers)
        logging.info(f'Successfully calculated average: {avg}')
        return avg
    except Exception as e:
        logging.error(f'Failed to calculate average: {e}')
        raise


# Пример использования
if __name__ == "__main__":
    while True:
        try:
            numbers = input("Enter a list of numbers separated by spaces: ")
            numbers = list(map(float, numbers.split()))
            average = calculate_average(numbers)
            print(f"The average is: {average}")
            break
        except ValueError as e:
            print(e)
            print("Please enter a valid list of numbers.")
