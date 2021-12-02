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

    counter_hor = 0
    counter_ver = 0

    for i in range(list_length):

        if i % 2 == 1:

            if value_list[i-1] == "forward":
                counter_hor += int(value_list[i])
            elif value_list[i-1] == "down":
                counter_ver += int(value_list[i])
            else:
                counter_ver -= int(value_list[i])

    return counter_ver * counter_hor


def part_2(value_list):
    list_length = len(value_list)

    counter_hor = 0
    counter_ver = 0
    counter_aim = 0

    for i in range(list_length):

        if i % 2 == 1:

            if value_list[i-1] == "forward":
                counter_hor += int(value_list[i])
                counter_ver += int(value_list[i]) * counter_aim
            elif value_list[i-1] == "down":
                counter_aim += int(value_list[i])
            else:
                counter_aim -= int(value_list[i])

    return counter_ver * counter_hor


if __name__ == '__main__':
    dir_path = os.path.dirname(os.path.realpath(__file__))

    input_read = read_file(dir_path + "/" + "input1.txt")

    value_list = input_read

    start_time = time.time()
    print("part 1: ", part_1(value_list))
    print("--- %s seconds ---" % (time.time() - start_time), "\n")

    start_time = time.time()
    print("part 2: ", part_2(value_list))
    print("--- %s seconds ---" % (time.time() - start_time), "\n")
