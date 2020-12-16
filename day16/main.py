import math
import numbers
import os
import re
import sys
import time
from collections import defaultdict

from utility.file_reader import read_file
from utility.parser import convert_to_int

fields = {
    'departure location': lambda x: 25 <= x <= 80 or 90 <= x <= 961,
    'departure station': lambda x: 41 <= x <= 133 or 148 <= x <= 968,
    'departure platform': lambda x: 48 <= x <= 425 or 451 <= x <= 952,
    'departure track': lambda x: 25 <= x <= 371 or 384 <= x <= 966,
    'departure date': lambda x: 49 <= x <= 531 or 546 <= x <= 973,
    'departure time': lambda x: 45 <= x <= 641 or 656 <= x <= 954,
    'arrival location': lambda x: 43 <= x <= 357 or 364 <= x <= 969,
    'arrival station': lambda x: 40 <= x <= 669 or 689 <= x <= 954,
    'arrival platform': lambda x: 40 <= x <= 550 or 570 <= x <= 956,
    'arrival track': lambda x: 49 <= x <= 854 or 863 <= x <= 953,
    'class': lambda x: 48 <= x <= 601 or 614 <= x <= 964,
    'duration': lambda x: 27 <= x <= 698 or 715 <= x <= 962,
    'price': lambda x: 38 <= x <= 781 or 800 <= x <= 970,
    'route': lambda x: 47 <= x <= 824 or 842 <= x <= 965,
    'row': lambda x: 45 <= x <= 219 or 241 <= x <= 955,
    'seat': lambda x: 47 <= x <= 388 or 401 <= x <= 954,
    'train': lambda x: 42 <= x <= 906 or 919 <= x <= 965,
    'type': lambda x: 40 <= x <= 726 or 733 <= x <= 955,
    'wagon': lambda x: 27 <= x <= 161 or 174 <= x <= 974,
    'zone': lambda x: 48 <= x <= 103 or 110 <= x <= 954
}


def part_1(value_list, scan_error=0):
    if len(value_list) == 0:
        return scan_error

    to_check = convert_to_int(value_list[0].split(','))

    for val in range(len(to_check)):
        found = False
        for k in fields:
            if fields.get(k, lambda x: False)(to_check[val]):
                found = True
                break
        if not found:
            scan_error += to_check[val]

    return part_1(value_list[1:], scan_error)


def part_2(value_list, value_list_parsed=None):
    if value_list_parsed is None:
        value_list_parsed = []

    if len(value_list) == 0:

        final = []

        for idx in range(len(value_list_parsed[0])):
            partial = []
            for idx2 in range(len(value_list_parsed)):
                partial.append(value_list_parsed[idx2][idx])
            final.append(partial)

        keys = defaultdict(list)

        for idx3 in range(len(final)):
            for k in fields:
                found = True
                for val in range(len(final[idx3])):
                    if not fields.get(k, lambda x: False)(final[idx3][val]):
                        found = False
                        break
                if found:
                    if not keys[idx3]:
                        to_append = []
                    else:
                        to_append = keys[idx3]

                    keys[idx3] = [*to_append, k]

        has_finished = False
        already_done = []

        while not has_finished:
            for k in keys:
                if k not in already_done and len(keys[k]) == 1:
                    already_done.append(k)
                    for k2 in keys:
                        if k is not k2 and keys[k][0] in keys[k2]:
                            keys[k2].remove(keys[k][0])

            for k_idx in keys:
                if len(keys[k_idx]) > 1:
                    has_finished = False
                    break
                else:
                    has_finished = True

        input_read = read_file(dir_path + "/" + "my.txt", ",")
        input_read = convert_to_int(input_read)

        total = 1

        for k in keys:
            if 'departure' in keys[k][0]:
                total *= input_read[k]

        return total

    to_check = convert_to_int(value_list[0].split(','))

    for val in range(len(to_check)):
        found = False
        for k in fields:
            if fields.get(k, lambda x: False)(to_check[val]):
                found = True
                break
        if not found:
            return part_2(value_list[1:], value_list_parsed)

    value_list_parsed.append(to_check)

    return part_2(value_list[1:], value_list_parsed)


if __name__ == '__main__':
    dir_path = os.path.dirname(os.path.realpath(__file__))

    input_read = read_file(dir_path + "/" + "nearby.txt", "\n")

    start_time = time.time()
    print('part 1:', part_1(input_read))
    print("--- %s seconds ---" % (time.time() - start_time), "\n")

    start_time = time.time()
    print('part 2:', part_2(input_read))
    print("--- %s seconds ---" % (time.time() - start_time), "\n")
