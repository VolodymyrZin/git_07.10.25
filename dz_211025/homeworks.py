def calculate_sum_from_file(filename):
    try:
        with open (filename, 'r') as file_obj:
            lines = file_obj.readlines()
            numbers = []
            for line in lines:
                line = line.strip()
                if line:
                    numbers.append(int(line))
            total = sum(numbers)
            return total
    except FileNotFoundError:
        return 'File not found'
    except ValueError:
         return "Invalid data in the file"


def sum_of_two_numbers(number1, number2):
    '''
    Function creates sum of two given numbers
    :param number1:
    :param number2:
    :return:
    '''
    result = number1 + number2
    return result

list_of_words = ['яка', 'приймає', 'два', 'рядки', 'та', 'повертає', 'індекс']
def longest_word(list_of_words):
    """
    Function creates longest word from given list of words
    :param list_of_words:
    :return:
    """
    return max(list_of_words, key=len)
