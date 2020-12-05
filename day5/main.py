import os
import time

from utility.file_reader import read_file
from utility.parser import convert_to_int


def path_traversal(value_list, right_step, down_step):
    path_idx = 0
    counter = 0

    path_length = len(value_list[0])

    for idx, value in enumerate(value_list):

        if idx % down_step == 0:
            single_path = value
            tree_or_space = single_path[path_idx]

            if tree_or_space == '#':
                counter += 1

            path_idx += right_step

            if path_idx >= path_length:
                path_idx = path_idx % path_length

    return counter


def part_1(value_list):
    right_3_down_1 = path_traversal(value_list, 3, 1)

    return right_3_down_1


def part_2(value_list):
    right_1_down_1 = path_traversal(value_list, 1, 1)
    right_3_down_1 = path_traversal(value_list, 3, 1)
    right_5_down_1 = path_traversal(value_list, 5, 1)
    right_7_down_1 = path_traversal(value_list, 7, 1)
    right_1_down_2 = path_traversal(value_list, 1, 2)

    return right_1_down_1 * right_1_down_2 * right_3_down_1 * right_5_down_1 * right_7_down_1


if __name__ == '__main__':
    dir_path = os.path.dirname(os.path.realpath(__file__))

    input_read = read_file(dir_path + "/" + "input1.txt")

    start_time = time.time()
    print('part 1:', part_1(input_read))
    print("--- %s seconds ---" % (time.time() - start_time), "\n")

    start_time = time.time()
    print('part 2:', part_2(input_read))
    print("--- %s seconds ---" % (time.time() - start_time), "\n")
