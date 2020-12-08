import math
import os
import re
import time

from utility.file_reader import read_file


def checker(value_list, override, already_visited=None, index=0, accumulator=0):
    if already_visited is None:
        already_visited = []

    for idx, val in enumerate(value_list[index:]):
        actual_index = idx + index
        if actual_index in already_visited:
            return False
        else:
            already_visited.append(actual_index)
            values = val.split()

            if override == actual_index:
                if values[0] == 'jmp':
                    continue
                elif values[0] == 'nop':
                    return checker(value_list, override, already_visited, actual_index + int(values[1]), accumulator)
            else:
                if values[0] == 'acc':
                    accumulator += int(values[1])
                elif values[0] == 'jmp':
                    return checker(value_list, override, already_visited, actual_index + int(values[1]), accumulator)
                elif values[0] == 'nop':
                    continue

    return True


def part_1(value_list, already_visited=None, index=0, accumulator=0):
    if already_visited is None:
        already_visited = []

    for idx, val in enumerate(value_list[index:]):
        actual_index = idx + index
        if actual_index in already_visited:
            return accumulator
        else:
            already_visited.append(actual_index)
            values = val.split()

            if values[0] == 'acc':
                accumulator += int(values[1])
            elif values[0] == 'jmp':
                return part_1(value_list, already_visited, actual_index + int(values[1]), accumulator)
            elif values[0] == 'nop':
                continue

    return accumulator


def part_2(value_list, already_visited=None, index=0, accumulator=0):
    if already_visited is None:
        already_visited = []

    if len(value_list) == 0:
        return "finished"

    for idx, val in enumerate(value_list[index:]):
        actual_index = idx + index
        if actual_index in already_visited:

            to_analyze = already_visited
            to_analyze.reverse()

            for an_idx in range(len(to_analyze)):
                current_value = value_list[to_analyze[an_idx]].split()
                if current_value[0] == 'acc':
                    continue
                else:
                    result = checker(value_list, to_analyze[an_idx])
                    if result:
                        return "change operation at: " + str(to_analyze[an_idx]) + " - " + str(
                            value_list[to_analyze[an_idx]])
        else:
            already_visited.append(actual_index)
            values = val.split()

            if values[0] == 'acc':
                accumulator += int(values[1])
                continue
            elif values[0] == 'jmp':
                return part_2(value_list, already_visited, actual_index + int(values[1]), accumulator)
            elif values[0] == 'nop':
                continue


if __name__ == '__main__':
    dir_path = os.path.dirname(os.path.realpath(__file__))

    input_read = read_file(dir_path + "/" + "input1.txt", "\n")
    input_read_2 = read_file(dir_path + "/" + "input_part2.txt", "\n")

    start_time = time.time()
    print('part 1:', part_1(input_read))
    print("--- %s seconds ---" % (time.time() - start_time), "\n")

    start_time = time.time()
    print(part_2(input_read))
    print('part 2:', part_1(input_read_2))
    print("--- %s seconds ---" % (time.time() - start_time), "\n")
