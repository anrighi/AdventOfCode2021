import math
import os
import time

from utility.file_reader import read_file


def lower_half(number):
    diff = (number[1] - number[0]) / 2
    return [number[0], math.floor(number[1] - diff)]


def upper_half(number):
    diff = (number[1] - number[0]) / 2
    return [math.ceil(diff + number[0]), number[1]]


def find_id(row_seat):
    row_length = len(row_seat)

    seat_row = [0, 127]
    seat_column = [0, 7]

    function_switcher = {
        'L': lower_half,
        'R': upper_half,
        'F': lower_half,
        'B': upper_half,
    }

    for idx in range(row_length):
        letter = row_seat[idx]
        if letter == 'R' or letter == 'L':
            seat_column = function_switcher[letter](seat_column)
        else:
            seat_row = function_switcher[letter](seat_row)

    return seat_row[0] * 8 + seat_column[0]


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
