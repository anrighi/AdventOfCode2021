import math
import os
import re
import time

from utility.file_reader import read_file
from utility.parser import convert_to_int
from utility.search import binary_search_recursive


def part_1(value_list):
    partial = value_list[:26]
    to_count = value_list[26]
    partial.sort()

    found = False

    for idx in range(len(partial)):
        diff = to_count - partial[idx]
        if binary_search_recursive(partial, diff, 0, len(partial) - 1) != -1:
            found = True
            break

    if found:
        return part_1(value_list[1:])
    else:
        return to_count


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

    start_time = time.time()
    print('part 1:', part_1(input_read))
    print("--- %s seconds ---" % (time.time() - start_time), "\n")

    start_time = time.time()
    print('part 2:', part_2(input_read))
    print("--- %s seconds ---" % (time.time() - start_time), "\n")
