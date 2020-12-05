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


def part_1(value_list, max_seat_id=0):
    if len(value_list) == 0:
        return max_seat_id

    seat_id = find_id(value_list[0])

    if seat_id > max_seat_id:
        return part_1(value_list[1:], seat_id)
    else:
        return part_1(value_list[1:], max_seat_id)


def part_2(value_list):
    list_length = len(value_list)
    seat_id_list = []

    for idx in range(list_length):
        seat_id = find_id(value_list[idx])
        seat_id_list.append(seat_id)

    seat_id_list.sort()

    for idx, val in enumerate(seat_id_list):
        if idx != val - seat_id_list[0]:
            return idx + seat_id_list[0]


if __name__ == '__main__':
    dir_path = os.path.dirname(os.path.realpath(__file__))

    input_read = read_file(dir_path + "/" + "input1.txt")

    start_time = time.time()
    print('part 1:', part_1(input_read))
    print("--- %s seconds ---" % (time.time() - start_time), "\n")

    start_time = time.time()
    print('part 2:', part_2(input_read))
    print("--- %s seconds ---" % (time.time() - start_time), "\n")
