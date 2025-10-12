class Rhombus:
    def __init__(self, side_a, angle_a):
        self.side_a = side_a
        self.angle_a = angle_a

    def __setattr__(self, key, value):
        if key == 'side_a':
            if not isinstance(value, (int, float)):
                print('side_a must be a number')
                value = None
            elif value <= 0:
                print('side_a cannot be negative or zero')
                value = None
            super().__setattr__(key, value)
            return
        if key == 'angle_a':
            if not isinstance(value, (int, float)):
                print('angle_a must be a number')
                value = None
            elif not (0 < value < 180):
                print('angle_a must be within the range (0, 180)')
                value = None
            super().__setattr__(key, value)
            return
        super().__setattr__(key, value)

    def get_angle_b(self):
        return 180 - self.angle_a
    angle_b = property(get_angle_b)


    def __str__(self):
        return f'Rhombus: side = {self.side_a}, angle A = {self.angle_a}, angle B = {self.angle_b}'

my_romb = Rhombus(10, 10)
print(my_romb)






































# # 🧪 Завдання: Клас Rectangle
#
# # 📋 Умова:
# # Створи клас Rectangle, який має:
# # - два атрибути: width і height
# # - метод area(), який повертає площу
# # - метод is_square(), який повертає True, якщо ширина дорівнює висоті
# # 🧠 Додатково:
# # - У конструкторі перевіряй, щоб width і height були додатні числа
# # - Якщо ні — виводь повідомлення і присвоюй None
#
# class Rectangle:
#     def __init__(self, width, height):
#             self.width = width
#             self.height = height
#
#     def __setattr__(self, key, value):
#         if key == 'width' or key == 'height':
#             if not isinstance(value, (int, float)):
#                 print('size must be a number')
#                 value = None
#             elif value <= 0:
#                 print('size cannot be negative or zero')
#                 value = None
#             super().__setattr__(key, value)
#             return
#
#     def area(self):
#         if self.width is None or self.height is None:
#             return None
#         return self.width * self.height
#
#     def  is_square(self):
#         if self.width == self.height:
#             return True
#         else:
#             return False
#     def perimeter(self):
#         return int(self.width + self.height) * 2
#
#     def __str__(self):
#         return f'Rectangle: width = {self.width}, height = {self.height}'
#
# my_rectangle = Rectangle(100, 100)
# print(my_rectangle)
# result = my_rectangle.perimeter()
# print(result)
#
#
#
# class Sphere:
#     def __init__(self, radius):
#         self.radius = radius
#
#     def volume(self):
#         return (4/3) * 3.14 * self.radius**3
#
#     def __str__(self):
#         return(f'The volume of sphere is: {self.volume()}')
#
# class Cube:
#     def __init__(self, side_length):
#         self.side_length = side_length
#
#     def volume(self):
#         return self.side_length**3
#
# class Cylinder:
#     def __init__(self, radius, height):
#         self.radius = radius
#         self.height = height
#
#     def volume(self):
#         return 3.14 * self.radius**2 * self.height
#
# def calculate_volume(obj):
#
#     return obj.volume()
#
# my_sphere = Sphere(3)
# print(my_sphere)
# my_cube = Cube(3)
# my_cylinder = Cylinder(2, 3)
#
# result_cyl = calculate_volume(my_cylinder)
# result_sphere = calculate_volume(my_sphere)
# result_cub = calculate_volume(my_cube)
# print(result_cyl)
# print(result_sphere)
# print(result_cub)
#
#
#
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __str__(self):
#         return(f'His name is {self.name}, his age ist{self.age}')
#
# my_person = Person('ji', 5)
# print(my_person)

