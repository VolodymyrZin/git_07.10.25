# Напишіть декоратор, який логує аргументи та результати викликаної функції.

import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


def log_args_and_result(function):
    def wrapper(*args, **kwargs):
        logging.debug(f'Called with args: {args}, kwargs:{kwargs}')
        result = function(*args, **kwargs)
        logging.debug(f'Returned result: {result}')
        return result

    return wrapper


# Створіть декоратор, який перехоплює та обробляє винятки, які виникають в ході виконання функції.


def exception_logger(function):
    def wrapper(*args, **kwargs):
        try:
            result = function(*args, **kwargs)
            return result
        except TypeError:
            logging.exception(f'Exception raised for args: {args}, kwargs:{kwargs}')
            return None
        except Exception as e:
            logging.exception(f'Exception raised: {e}')
            print("Incorrect type of arguments")
            return None

    return wrapper


@log_args_and_result
@exception_logger
def is_even(num):
    if not isinstance(num, int):
        raise TypeError("Argument must be an integer")
    return num % 2 == 0


is_even(454.0)
