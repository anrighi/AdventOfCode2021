import os

dir_path = os.path.dirname(os.path.realpath(__file__))


def read_file(file_path):
    f = open(dir_path + "/" + file_path, "r")
    return f.read().split()


def convert_to_int(string_list):
    for i in range(len(string_list)):
        string_list[i] = int(string_list[i])
    return string_list


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
    input_read = read_file("input1.txt")

    value_list = convert_to_int(input_read)
    value_list.sort()

    print("part 1: ", part_1(value_list))
    print("part 2: ", part_2(value_list))
