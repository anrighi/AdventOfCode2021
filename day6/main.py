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


def fish_spawner(value_list, days):
    fish_list = value_list

    for i in range(days):

        new_list = []

        for j in range(len(fish_list)):

            if fish_list[j] == 0:
                new_list.append(6)
                new_list.append(8)
            else:
                new_list.append(fish_list[j] - 1)

        fish_list = new_list

    return len(fish_list)


def fish_spawner_opt(value_list, days):

    fishes = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    for i in range(len(value_list)):
        fishes[value_list[i]] += 1

    for i in range(days):

        new_fishes = [0, 0, 0, 0, 0, 0, 0, 0, 0]

        for j, e in reversed(list(enumerate(fishes))):

            if j == 0:
                new_fishes[6] += e
                new_fishes[8] += e
            else:
                new_fishes[j - 1] += e

        fishes = new_fishes

    return sum(fishes)


def part_1(value_list):
    return fish_spawner_opt(value_list, 80)


def part_2(value_list):
    return fish_spawner_opt(value_list, 256)


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
