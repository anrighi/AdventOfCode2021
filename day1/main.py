import time
import os

from utility.file_reader import read_file
from utility.parser import convert_to_int
from utility.search import binary_search_recursive


def part_1(value_list):
    list_length = len(value_list)

    for i in range(list_length):
        for k in range(list_length):
            if value_list[i] + value_list[k] == 2020:
                return value_list[i] * value_list[k]


def part_1_binary_search(value_list):
    list_length = len(value_list)

    for i in range(list_length):
        idx = binary_search_recursive(value_list, 2020 - value_list[i], i, list_length)

        if idx != -1:
            return value_list[i] * value_list[idx]


def part_2(value_list):
    list_length = len(value_list)

    for i in range(list_length):
        for k in range(list_length):
            for l in range(list_length):
                if value_list[i] + value_list[k] + value_list[l] == 2020:
                    return value_list[i] * value_list[k] * value_list[l]


def part_2_w_range(value_list):
    list_length = len(value_list)

    for i in range(list_length):
        for k in range(i + 1, list_length):
            for l in range(k + 1, list_length):
                if value_list[i] + value_list[k] + value_list[l] == 2020:
                    return value_list[i] * value_list[k] * value_list[l]


def part_2_binary_search(value_list):
    list_length = len(value_list)

    for i in range(list_length):
        for k in range(i + 1, list_length):
            idx = binary_search_recursive(value_list, 2020 - value_list[i] - value_list[k], k, list_length)

            if idx != -1:
                return value_list[i] * value_list[k] * value_list[idx]


if __name__ == '__main__':
    dir_path = os.path.dirname(os.path.realpath(__file__))

    input_read = read_file(dir_path + "/" + "input1.txt")

    value_list = convert_to_int(input_read)
    value_list.sort()

    start_time = time.time()
    print("part 1: ", part_1(value_list))
    print("--- %s seconds ---" % (time.time() - start_time), "\n")

    start_time = time.time()
    print("part 1 // binary search: ", part_1_binary_search(value_list))
    print("--- %s seconds ---" % (time.time() - start_time), "\n")

    start_time = time.time()
    print("part 2: ", part_2(value_list))
    print("--- %s seconds ---" % (time.time() - start_time), "\n")

    start_time = time.time()
    print("part 2 // range correct: ", part_2_w_range(value_list))
    print("--- %s seconds ---" % (time.time() - start_time), "\n")

    start_time = time.time()
    print("part 2 // binary search: ", part_2_binary_search(value_list))
    print("--- %s seconds ---" % (time.time() - start_time), "\n")
