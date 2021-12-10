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

    risk = 0

    for i in range(len(value_list)):
        for j in range(len(value_list[i])):
            upper = value_list[i][j] < value_list[i-1][j] if i >= 1 else True
            bottom = value_list[i][j] < value_list[i+1][j] if i < (len(value_list) -
                                                                   1) else True
            left = value_list[i][j] < value_list[i][j-1] if j >= 1 else True
            right = value_list[i][j] < value_list[i][j+1] if j < (
                len(value_list[i]) - 1) else True

            if upper and bottom and left and right:
                risk += int(value_list[i][j]) + 1

    return risk


def part_2(value_list):

    score = []

    for i in range(len(value_list)):
        for j in range(len(value_list[i])):
            upper = value_list[i][j] < value_list[i-1][j] if i >= 1 else True
            bottom = value_list[i][j] < value_list[i+1][j] if i < (len(value_list) -
                                                                   1) else True
            left = value_list[i][j] < value_list[i][j-1] if j >= 1 else True
            right = value_list[i][j] < value_list[i][j+1] if j < (
                len(value_list[i]) - 1) else True

            if upper and bottom and left and right:
                risk += int(value_list[i][j]) + 1

    return score[len(score) // 2]


if __name__ == '__main__':
    dir_path = os.path.dirname(os.path.realpath(__file__))

    input_read = read_file(dir_path + "/" + "input1.txt")

    value_list = []

    for i in range(len(input_read)):
        value_list.append([char for char in input_read[i]])

    start_time = time.time()
    print("part 1: ", part_1(value_list))
    print("--- %s seconds ---" % (time.time() - start_time), "\n")

    start_time = time.time()
    #print("part 2: ", part_2(value_list))
    print("--- %s seconds ---" % (time.time() - start_time), "\n")
