# Генератори:
#
# Напишіть генератор, який повертає послідовність парних чисел від 0 до N.
def even_numbers(n):
    for number in range(n + 1):
        if number % 2 == 0:
            yield number

for num in even_numbers(10):
    print(num)

# Створіть генератор, який генерує послідовність Фібоначчі до певного числа N.
def fibonacci(n):
    a, b = 0, 1
    while a < n:
        yield a
        a, b = b, a + b

for num in fibonacci(100):
    print(num)

