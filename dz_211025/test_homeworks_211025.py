

import unittest
from dz_211025.homeworks import calculate_sum_from_file, sum_of_two_numbers, longest_word

class TestHomeworks(unittest.TestCase):

    def test_sum_of_two_numbers(self):
        self.assertEqual(sum_of_two_numbers(3, 4), 7)
        self.assertEqual(sum_of_two_numbers(-1, 1), 0)
        self.assertEqual(sum_of_two_numbers(0, 0), 0)
        self.assertEqual(sum_of_two_numbers(-5, -10), -15)

    def test_longest_word(self):
        self.assertEqual(longest_word(['яка', 'приймає', '        ', 'рядки']), '        ')
        self.assertEqual(longest_word(['один', 'дваа', 'трии']), 'один')
        self.assertEqual(longest_word(['']), '')

    def test_calculate_sum_from_file(self):
        self.assertEqual(calculate_sum_from_file('dz_211025/tst.txt'), 'File not found')
        self.assertEqual(calculate_sum_from_file('dz_211025/test.txt'), 45)
        self.assertIsInstance(calculate_sum_from_file('dz_211025/test.txt'), int)

if __name__ == '__main__':
    unittest.main()
