import os
import sys
import time

from utility.file_reader import read_file
from utility.parser import convert_to_int


def filter_values(val):
    return val.isnumeric()


def part_1(value_list, timestamp=1000340):
    value_list = list(filter(filter_values, value_list.split(',')))
    value_list = convert_to_int(value_list)

    best = sys.maxsize
    to_return = 0

    for idx in range(len(value_list)):
        if value_list[idx] - (timestamp % value_list[idx]) < best:
            to_return = value_list[idx]
            best = value_list[idx] - (timestamp % value_list[idx])

    return best * to_return


def part_2(value_list, timestamp=1000340):
    value_list = (value_list.split(','))

    okay = False
    counter = value_list[0]

    while not okay:
        for idx, val in enumerate(value_list):
            if val is not 'x':



                return

        okay = True

    return


if __name__ == '__main__':
    dir_path = os.path.dirname(os.path.realpath(__file__))

    input_read = read_file(dir_path + "/" + "input1.txt", "\n")

    start_time = time.time()
    print('part 1:', part_1(input_read[1]))
    print("--- %s seconds ---" % (time.time() - start_time), "\n")

    start_time = time.time()
    print('part 2:', part_2(input_read[1]))
    print("--- %s seconds ---" % (time.time() - start_time), "\n")
