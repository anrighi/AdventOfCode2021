import os
import time
from typing import Counter


def convert_to_int(string_list):
    for i in range(len(string_list)):
        string_list[i] = int(string_list[i])
    return string_list


def read_file(file_path, optional_divider=None):
    f = open(file_path, "r")
    if optional_divider is not None:
        return f.read().split(optional_divider)
    else:
        return f.read().split()


def part_1(value_list):

    list.sort(value_list)

    frequency = []

    j = 0

    while j < 1912:
        frequency.append(0)
        j += 1

    for i in range(len(value_list)):
        frequency[value_list[i]] += 1

    min_value = 1000000

    for i in range(len(frequency)):
        current_value = 0

        for j in range(len(frequency)):
            if j != i:
                current_value += frequency[j] * abs(j - i)

        if current_value < min_value:
            min_value = current_value

    return min_value


def part_2(value_list):
    list.sort(value_list)

    frequency = []

    j = 0

    while j < 1912:
        frequency.append(0)
        j += 1

    for i in range(len(value_list)):
        frequency[value_list[i]] += 1

    min_value = 1000000000000000000

    for i in range(len(frequency)):
        current_value = 0

        for j in range(len(frequency)):
            if j != i:
                distance = abs(j - i)
                counter = 1

                while counter <= distance:
                    current_value += frequency[j] * counter
                    counter += 1

        if current_value < min_value:
            min_value = current_value

    return min_value


if __name__ == '__main__':
    dir_path = os.path.dirname(os.path.realpath(__file__))

    input_read = read_file(dir_path + "/" + "input1.txt", ",")

    value_list = convert_to_int(input_read)

    start_time = time.time()
    print("part 1: ", part_1(value_list))
    print("--- %s seconds ---" % (time.time() - start_time), "\n")

    start_time = time.time()
    print("part 2: ", part_2(value_list))
    print("--- %s seconds ---" % (time.time() - start_time), "\n")
