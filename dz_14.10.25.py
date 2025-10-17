# Завдання 1
#
# Створіть клас Employee, який має атрибути name та salary. Далі створіть два класи, Manager та Developer, які успадковуються від Employee. Клас Manager повинен мати
# додатковий атрибут department, а клас Developer - атрибут programming_language.
#
# Тепер створіть клас TeamLead, який успадковується як від Manager, так і від Developer. Цей клас представляє керівника з команди розробників. Клас TeamLead повинен
# мати всі атрибути як Manager (ім'я, зарплата, відділ), а також атрибут team_size, який вказує на кількість розробників у команді, якою керує керівник.

class Employee:
    def __init__(self, *args, **kwargs):
        self.name = kwargs.get('name')
        self.salary = kwargs.get('salary')

class Manager(Employee):
    def __init__(self, *args, **kwargs):
        super().__init__( *args, **kwargs)
        self.department = kwargs.get('department')


class Developer(Employee):
    def __init__(self, *args, **kwargs):
        super().__init__( *args, **kwargs)
        self.programming_language = kwargs.get('programming_language')


class TeamLeader(Manager, Developer):
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.team_size = kwargs.get('team_size')


    def leader(self):
        return self.name, self.salary, self.department, self.programming_language, self.team_size

    def __str__(self):
        return (f"Ім'я тімліда: {self.name}, має зарплатню: {self.salary}, рідна мова: {self.programming_language}, кількість підлеглих в команді: {self.team_size}")

lead = TeamLeader(name='Erema', salary=100, department='video', programming_language='Python', team_size=10)
print(lead)



# Завдання 2
#
# Створіть абстрактний клас "Фігура" з абстрактними методами для отримання площі та периметру. Наслідуйте від нього декілька
# (> 2) інших фігур, та реалізуйте математично вірні для них методи для площі та периметру. Властивості по типу
# “довжина сторони” й т.д. повинні бути приватними, та ініціалізуватись через конструктор. Створіть Декілька різних
# об’єктів фігур, та у циклі порахуйте та виведіть в консоль площу та периметр кожної.

from abc import ABC, abstractmethod

class Figure(ABC):

    def __init__(self):
        super().__init__()

    @abstractmethod
    def square(self):
        raise AttributeError('square must be implemented')

    @abstractmethod
    def perimeter(self):
        raise AttributeError('perimeter must be implemented')

class Triangle(Figure):

    def __init__(self, figure_width, figure_height, figure_side):
        super().__init__()
        self.size(figure_width, figure_height, figure_side)
        self.__figure_width = figure_width
        self.__figure_height = figure_height
        self.__figure_side = figure_side

    def square(self):
        square = (self.__figure_width * self.__figure_height) / 2
        return square

    def perimeter(self):
        perimeter = self.__figure_width + self.__figure_height + self.__figure_side
        return perimeter

    def size(self, width, height, side):
        if width <= 0 or height <= 0 or side <= 0:
            raise ValueError('size must be positive and not equal to 0')

    def __str__(self):
        return f"Трикутник зі сторонами: {self.__figure_width}, {self.__figure_height}, {self.__figure_side}; периметр = {self.perimeter()}; площа = {self.square()}"


class Circle(Figure):

    def __init__(self, figure_radius):
        super().__init__()
        self.size(figure_radius)
        self.__figure_radius = figure_radius

    def square(self):
        square = self.__figure_radius ** 2 * 3.14
        return square

    def perimeter(self):
        perimeter = self.__figure_radius * 3.14 * 2
        return perimeter

    def size(self, value):
        if value <= 0:
            raise ValueError('size must be positive and not equal to 0')

    def __str__(self):
        return f"Коло з радіусом: {self.__figure_radius}; периметр = {self.perimeter()}; площа = {self.square()}"

class Rectangle(Figure):

    def __init__(self, figure_width, figure_height):
        super().__init__()
        self.size(figure_width, figure_height)
        self.__figure_width = figure_width
        self.__figure_height = figure_height

    def square(self):
        square = self.__figure_width * self.__figure_height
        return square

    def perimeter(self):
        perimeter = (self.__figure_width + self.__figure_height) * 2
        return perimeter

    def size(self, width, height):
        if width <= 0 or height <= 0:
            raise ValueError('size must be positive and not equal to 0')

    def __str__(self):
        return f"Прямокутник зі сторонами: {self.__figure_width}, {self.__figure_height}; периметр = {self.perimeter()}; площа = {self.square()}"

my_square_triangle = Triangle(10, 10, 10)
# print(my_square_triangle)

my_square_circle = Circle(10)
# print(my_square_circle)

my_square_rectangle = Rectangle(10, 10)
# print(my_square_rectangle)

list_objects = [
    my_square_triangle,
    my_square_circle,
    my_square_rectangle,
]
print(f'Кількість фігур = {len(list_objects)}')

for obj in list_objects:
    print(obj)


