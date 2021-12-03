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

    most_common = []
    least_common = []

    string_length = len(value_list[0])

    for j in range(string_length):

        ones = 0
        zeros = 0

        for i in range(list_length):
            if (value_list[i][j] == "1"):
                ones += 1
            else:
                zeros += 1

        if ones > zeros:
            most_common.append(1)
            least_common.append(0)
        else:
            most_common.append(0)
            least_common.append(1)

    return int("".join(str(x) for x in most_common), 2) * int("".join(str(x) for x in least_common), 2)


def find_most_least_common(index, list):

    ones = 0
    zeros = 0

    most_common = []
    least_common = []

    for i in range(len(list)):
        if (list[i][index] == "1"):
            ones += 1
        else:
            zeros += 1

    if ones >= zeros:
        most_common.append(1)
        least_common.append(0)
    else:
        most_common.append(0)
        least_common.append(1)

    return [most_common[0], least_common[0]]


def part_2(value_list):

    ox_list = value_list
    co_list = value_list

    most_common = []
    least_common = []

    string_length = len(value_list[0])

    for j in range(string_length):

        res = find_most_least_common(j, ox_list)

        most_common = res[0]

        new_ox_list = []

        if (len(ox_list) > 1):

            for i in range(len(ox_list)):

                if (int(ox_list[i][j]) == int(most_common)):
                    new_ox_list.append(ox_list[i])

            ox_list = new_ox_list

    for j in range(string_length):

        res = find_most_least_common(j, co_list)

        least_common = res[1]

        new_co_list = []

        if (len(co_list) > 1):

            for i in range(len(co_list)):

                if (int(co_list[i][j]) == int(least_common)):
                    new_co_list.append(co_list[i])

            co_list = new_co_list

    return int(ox_list[0], 2) * int(co_list[0], 2)


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
