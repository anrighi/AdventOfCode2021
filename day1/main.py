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
    list_length = len(value_list)

    current_value = value_list[0]
    counter = 0

    for i in range(list_length):

        if value_list[i] > current_value:
            counter += 1

        current_value = value_list[i]

    return counter


def part_2(value_list):
    list_length = len(value_list)

    current_sum = value_list[0] + value_list[1] + value_list[2]
    counter = 0

    for i in range(list_length):

        if i >= 3:

            this_sum = value_list[i] + value_list[i - 1] + value_list[i - 2]

            if this_sum > current_sum:
                counter += 1

            current_sum = this_sum

    return counter


if __name__ == '__main__':
    dir_path = os.path.dirname(os.path.realpath(__file__))

    input_read = read_file(dir_path + "/" + "input1.txt")

    value_list = convert_to_int(input_read)

    start_time = time.time()
    print("part 1: ", part_1(value_list))
    print("--- %s seconds ---" % (time.time() - start_time), "\n")

    start_time = time.time()
    print("part 2: ", part_2(value_list))
    print("--- %s seconds ---" % (time.time() - start_time), "\n")
