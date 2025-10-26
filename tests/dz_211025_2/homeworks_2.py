
list_numbers = []
def average(list_numbers):
    if not list_numbers:
        return 0.0
    average_number = sum(list_numbers) / len(list_numbers)
    return average_number



dict_of_users = {}
def adults(dict_of_users):
    if not dict_of_users:
        return []
    return [id for id, age in dict_of_users.items() if age > 18]

def is_even(number):
    return number % 2 == 0

def get_max_value(dict_of_values):
    if not dict_of_values:
        raise ValueError
    return max(dict_of_values, key=dict_of_values.get)

def validate_password(password):
    if len(password) < 8:
        return False
    has_letter = any(char.isalpha() for char in password)
    has_digit = any(char.isdigit() for char in password)
    return has_letter and has_digit

def is_valid_email(email):
    if not isinstance(email, str):
        return False
    if '@' not in email or email.startswith('@') or email.endswith('@'):
        return False
    if '.' not in email or email.startswith('.') or email.endswith('.'):
        return False
    return True

def is_prime(n):
    if not isinstance(n, int) or n < 2 :
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True






