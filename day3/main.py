import os

from utility.file_reader import read_file
from utility.parser import convert_to_int


def part_1(value_list):
    counter = 0

    for idx, value in enumerate(value_list):
        if idx % 3 == 0:
            value_range = convert_to_int(value.split('-'))

            letter = value_list[idx + 1][0:1]
            password = value_list[idx + 2]

            letter_occurrences = password.count(letter)

            if value_range[0] <= letter_occurrences <= value_range[1]:
                counter += 1

    return counter


# RecursionError: maximum recursion depth exceeded while calling a Python object
def part_1_recursive(value_list, counter):
    print(len(value_list))

    if len(value_list) == 0:
        return counter
    else:
        value_range = convert_to_int(value_list[0].split('-'))
        letter = value_list[1][0:1]
        password = value_list[2]

        letter_occurrences = password.count(letter)

        if value_range[0] <= letter_occurrences <= value_range[1]:
            counter += 1

        return part_1_recursive(value_list[3:], counter)


def part_2(value_list):
    counter = 0

    for idx, value in enumerate(value_list):
        if idx % 3 == 0:
            value_range = convert_to_int(value.split('-'))

            letter = value_list[idx + 1][0:1]
            password = value_list[idx + 2]

            idx0 = value_range[0] - 1
            idx1 = value_range[1] - 1

            if password[idx0] == letter or password[idx1] == letter:
                if password[idx0] != password[idx1]:
                    counter += 1

    return counter


if __name__ == '__main__':
    dir_path = os.path.dirname(os.path.realpath(__file__))

    input_read = read_file(dir_path + "/" + "input1.txt")

    print('part 1:', part_1(input_read))
    print('part 2:', part_2(input_read))
