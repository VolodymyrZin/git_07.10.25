# Створіть масив зі строками, які будуть складатися з чисел, які розділені комою. Наприклад:#
# [”1,2,3,4”, ”1,2,3,4,50” ”qwerty1,2,3”]#
# Для кожного елементу списку виведіть суму всіх чисел (створіть нову функцію для цього).#
# Якщо є символи, що не є числами (”qwerty1,2,3” у прикладі), вам потрібно зловити вийняток і вивести “Не можу це зробити!”#
# Використовуйте блок try\except, щоб уникнути інших символів, окрім чисел у списку.#
# Для цього прикладу правильний вивід буде - 10, 60, “Не можу це зробити”

list_of_string = [
    '1,2,3,4',
    '1,2,3,4,50',
    'qwerty1,2,3',
    '5,6,7,8',
    'qwerty5,6,7',
]
def sum_of_numbers(list_of_string):
    list_of_numbers = []
    for item in list_of_string:
        parts = item.split(',')
        total_number = 0
        try:
            for part in parts:
                total_number += int(part)
            list_of_numbers.append(total_number)
        except ValueError:
            list_of_numbers.append("it is not int")
    return list_of_numbers

print(sum_of_numbers(list_of_string)) 
































