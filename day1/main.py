from utility.file_reader import read_file
import os

from utility.parser import convert_to_int


def part_1(value_list):
    list_length = len(value_list)

    for i in range(list_length):
        for k in range(list_length):
            if value_list[i] + value_list[k] == 2020:
                return value_list[i] * value_list[k]


def part_2(value_list):
    list_length = len(value_list)

    for i in range(list_length):
        for k in range(list_length):
            for l in range(list_length):
                if value_list[i] + value_list[k] + value_list[l] == 2020:
                    return value_list[i] * value_list[k] * value_list[l]


if __name__ == '__main__':
    dir_path = os.path.dirname(os.path.realpath(__file__))

    input_read = read_file(dir_path + "/" + "input1.txt")

    value_list = convert_to_int(input_read)
    value_list.sort()

    print("part 1: ", part_1(value_list))
    print("part 2: ", part_2(value_list))