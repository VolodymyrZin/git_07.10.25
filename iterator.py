# Реалізуйте ітератор для зворотного виведення елементів списку.

class ReverseIterator:

    def __init__(self, lst):
        self.lst = lst
        self.index = len(lst) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < 0:
            raise StopIteration
        value = self.lst[self.index]
        self.index -= 1
        return value


lst = [2, 4, 80, 100]
for i in ReverseIterator(lst):
    print(i)
print('_' * 80)


# Напишіть ітератор, який повертає всі парні числа в діапазоні від 0 до N.

class EvenNumbersIterator:
    def __init__(self, number):
        self.number = number
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):

        while self.index <= self.number:
            n = self.index
            self.index += 2
            if n % 2 == 0:
                return n
        raise StopIteration


for even in EvenNumbersIterator(10):
    print(even)























