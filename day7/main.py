import math
import os
import re
import time

from utility.file_reader import read_file


def find_contains_bag(value_list, to_search):
    add_to_search = []

    for rule in range(len(value_list)):
        contains_contained = value_list[rule].split('contain')

        contains = contains_contained[0]
        contained = contains_contained[1].split(',')

        if any(to_search in bags for bags in contained):
            to_add_val = re.sub("bags|bag", "", contains).strip()
            add_to_search.append(to_add_val)

    return add_to_search


def part_1(value_list, to_search=None):
    if to_search is None:
        to_search = []

    add_to_search = []

    if not to_search:
        add_to_search.extend(find_contains_bag(value_list, "shiny gold"))
    else:
        for search_index in range(len(to_search)):
            add_to_search.extend(find_contains_bag(value_list, to_search[search_index]))

    new_list = to_search + list(set(add_to_search) - set(to_search))

    if new_list == to_search:
        return len(to_search)
    else:
        return part_1(value_list, new_list)


def find_contained_bags(value_list, search_val):
    total = 0

    for rule in range(len(value_list)):
        contains_contained = value_list[rule].split('contain')
        contains = contains_contained[0]

        if search_val in contains:
            contained = contains_contained[1].split(',')
            for contained_bags in range(len(contained)):
                if "no other" in contained[contained_bags]:
                    return 0
                else:
                    string_divided = re.search("(\d)\s(\w+\s\w+)", contained[contained_bags])
                    counter = int(string_divided[1])
                    to_add_val = string_divided[2]
                    total += counter + counter * find_contained_bags(value_list, to_add_val)
    return total


def part_2(value_list):
    return find_contained_bags(value_list, "shiny gold")


if __name__ == '__main__':
    dir_path = os.path.dirname(os.path.realpath(__file__))

    input_read = read_file(dir_path + "/" + "input1.txt", "\n")

    start_time = time.time()
    print('part 1:', part_1(input_read))
    print("--- %s seconds ---" % (time.time() - start_time), "\n")

    start_time = time.time()
    print('part 2:', part_2(input_read))
    print("--- %s seconds ---" % (time.time() - start_time), "\n")
