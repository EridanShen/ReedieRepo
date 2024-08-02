import logging
import random

# Настройка логирования
logging.basicConfig(filename='rng_generator.log', level=logging.INFO, format='%(asctime)s %(message)s')

def generate_random_number(start, end):
    try:
        logging.info(f'Trying to generate random number in range {start} to {end}')
        if start < 0 or end < 0 or start > end:
            raise ValueError("Invalid range. Start and end must be non-negative and start must be less than or equal to end.")
        number = random.randint(start, end)
        logging.info(f'Successfully generated number: {number}')
        return number
    except Exception as e:
        logging.error(f'Failed to generate random number: {e}')
        raise

