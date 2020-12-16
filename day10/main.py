import math
import os
import re
import time
from collections import Counter

from utility.file_reader import read_file
from utility.parser import convert_to_int
from utility.search import binary_search_recursive


def part_1(value_list, total=None, counter=0):
    if total is None:
        total = []

    if len(value_list) == 0:
        total.append(3)

        values = Counter(total)
        return values[1] * values[3]

    if value_list[0] - counter == 3:
        total.append(3)
    else:
        total.append(1)

    return part_1(value_list[1:], total, value_list[0])


def part_2(value_list):
    counter = 0
    idx = 0

    while counter < 393911906:
        counter += value_list[idx]
        idx += 1

    if counter == 393911906:
        partial = value_list[:idx]
        partial.sort()
        return partial[0] + partial[len(partial) - 1]
    else:
        return part_2(value_list[1:])


if __name__ == '__main__':
    dir_path = os.path.dirname(os.path.realpath(__file__))

    input_read = read_file(dir_path + "/" + "input1.txt", "\n")

    input_read = convert_to_int(input_read)

    input_read.sort()

    start_time = time.time()
    print('part 1:', part_1(input_read))
    print("--- %s seconds ---" % (time.time() - start_time), "\n")

    start_time = time.time()
    # print('part 2:', part_2(input_read))
    print("--- %s seconds ---" % (time.time() - start_time), "\n")
