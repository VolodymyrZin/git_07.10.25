
import pytest

from tests.dz_211025_2.homeworks_2 import (average, adults, is_even, get_max_value,
                                           validate_password, is_valid_email, is_prime)


@pytest.mark.tests
class TestHomeworks_2:

    @pytest.mark.parametrize('list_numbers, expected', [
        ([10,20,30], 20.0),
        ([0,-1,-2], -1.0),
        ([], 0.0),
        ([100], 100.0),
        ([1.5, 2.5, 3.5], 2.5),
    ])
    @pytest.mark.average
    def test_average(self, list_numbers, expected):
        actual_result = average(list_numbers)
        assert actual_result == expected

    @pytest.mark.parametrize('dict_of_users, expected', [
        ({'1': 18, '2': 19, '3': 20}, ['2', '3']),
        ({'1':18}, []),
        ({'1':17}, []),
        ({'1':19}, ['1']),
        ({}, []),
    ])
    @pytest.mark.adults
    def test_adults(self, dict_of_users, expected):
        actual_result = adults(dict_of_users)
        assert actual_result == expected

    @pytest.mark.parametrize('number, expected', [
    (3, False),
    (4, True),
    (1, False),
    (-1, False),
    (0, True),
    (-4, True),
    ])

    @pytest.mark.is_even
    def test_is_even(self, number, expected):
        actual_result = is_even(number)
        assert actual_result == expected

    @pytest.mark.parametrize('dict_of_values, expected', [
        ({'1': 18, '2': 19, '3': -20}, '2'),
        ({'1': 18, '2': 18, '3': 2}, '1'),
        ({'1': 18}, '1'),
    ])
    @pytest.mark.max_value
    def test_get_max_value(self, dict_of_values, expected):
        actual_result = get_max_value(dict_of_values)
        assert actual_result == expected

    @pytest.mark.parametrize('password, expected', [
        ('3', False),
        ('4ghfgjjh8', True),
        ('', False),
        ('8h', False),

    ])
    @pytest.mark.validate_password
    def test_validate_password(self, password, expected):
        actual_result = validate_password(password)
        assert actual_result == expected


    @pytest.mark.parametrize('email, expected', [
        ('', False),
        ('example@i.ua', True),
        ('@i.ua', False),
        ('example@', False),
        ('.ua', False),
        ('example@i.', False),
    ])

    @pytest.mark.is_valid_email
    def test_is_valid_email(self, email, expected):
        actual_result = is_valid_email(email)
        assert actual_result == expected

    @pytest.mark.parametrize('number, expected', [
        (3, True),
        ('3', False),
        (-3, False),
        (2, True),
        (4, False),
        (1, False),
        (-1, False),
        (0, False),
        ([], False),
    ])

    @pytest.mark.is_prime
    def test_is_prime(self, number, expected):
        actual_result = is_prime(number)
        assert actual_result == expected



