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


# implemented from https://stackabuse.com/binary-search-in-python/
def binary_search_recursive(array, element, start, end):
    if start > end:
        return -1

    mid = (start + end) // 2
    if element == array[mid][0]:
        return mid

    if element < array[mid][0]:
        return binary_search_recursive(array, element, start, mid - 1)
    else:
        return binary_search_recursive(array, element, mid + 1, end)


def part_1(value_list):

    polymer = "CVKKFSSNNHNPSPPKBHPB"
    steps = 0

    while steps < 10:

        new_polymer = ""

        for i in range(len(polymer) - 1):

            new_polymer += polymer[i]

            for j in range(len(value_list)):

                char_value = value_list[j].split(" -> ")

                if polymer[i : i + 2] == char_value[0]:
                    new_polymer += char_value[1]
                    break

        new_polymer += polymer[-1]

        steps += 1
        polymer = new_polymer

    frequency = {}

    for char in range(len(polymer)):
        if polymer[char] in frequency:
            frequency[polymer[char]] += 1
        else:
            frequency[polymer[char]] = 1

    return max(dict.values(frequency)) - min(dict.values(frequency))


def part_2(value_list):

    polymer = "CVKKFSSNNHNPSPPKBHPB"
    steps = 0

    values_splitted = {}

    for j in range(len(value_list)):
        char_value = value_list[j].split(" -> ")
        values_splitted[char_value[0]] = char_value[1]

    while steps < 40:

        print("Step:", steps, " - polymer length", len(polymer))

        new_polymer = ""

        for i in range(len(polymer) - 1):

            new_polymer += polymer[i]

            if polymer[i : i + 2] in values_splitted:
                new_polymer += values_splitted[polymer[i : i + 2]]

        new_polymer += polymer[-1]

        polymer = new_polymer
        steps += 1

    frequency = {i: polymer.count(i) for i in set(polymer)}
    return max(dict.values(frequency)) - min(dict.values(frequency))


if __name__ == "__main__":
    dir_path = os.path.dirname(os.path.realpath(__file__))

    input_read = read_file(dir_path + "/" + "input1.txt", "\n")

    value_list = input_read

    start_time = time.time()
    print("part 1: ", part_1(value_list))
    print("--- %s seconds ---" % (time.time() - start_time), "\n")

    start_time = time.time()
    print("part 2: ", part_2(value_list))
    print("--- %s seconds ---" % (time.time() - start_time), "\n")
