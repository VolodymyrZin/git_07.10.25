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
                super().__setattr__('angle_b', None)
            elif not (0 < value < 180):
                print('angle_a must be within the range (0, 180)')
                value = None
                super().__setattr__('angle_b', None)
            else:
                super().__setattr__('angle_b', 180 - value)
            super().__setattr__('angle_a', value)
            return
        super().__setattr__(key, value)

    def __str__(self):
        return f'Rhombus: side = {self.side_a}, angle A = {self.angle_a}, angle B = {self.angle_b}'

my_rhombus = Rhombus(20, 90)
print(my_rhombus)