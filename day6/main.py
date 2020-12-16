import math
import os
import time

from utility.file_reader import read_file


def part_1(value_list, total=0):
    if len(value_list) == 0:
        return total

    group = value_list[0].split()

    answers = []

    for idx in range(len(group)):
        single_form = group[idx]
        for letter_idx, letter in enumerate(single_form):
            if letter not in answers:
                answers.append(letter)

    return part_1(value_list[1:], total + len(answers))


def part_2(value_list, total=0):
    if len(value_list) == 0:
        return total

    group = value_list[0].split()
    group_answers = []

    for idx in range(len(group)):
        single_form = group[idx]
        single_answers = list(set(list(single_form)))

        if idx == 0:
            group_answers = single_answers
        else:
            group_answers = list(set(group_answers) & set(single_answers))

    return part_2(value_list[1:], total + len(group_answers))


if __name__ == '__main__':
    dir_path = os.path.dirname(os.path.realpath(__file__))

    input_read = read_file(dir_path + "/" + "input1.txt", "\n\n")

    start_time = time.time()
    print('part 1:', part_1(input_read))
    print("--- %s seconds ---" % (time.time() - start_time), "\n")

    start_time = time.time()
    print('part 2:', part_2(input_read))
    print("--- %s seconds ---" % (time.time() - start_time), "\n")
