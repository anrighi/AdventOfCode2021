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


def line_checker(line):

    scores = {
        ")":  3,
        "]": 57,
        "}":  1197,
        ">":  25137,
    }

    closure = []

    for i in range(len(line)):

        if line[i] == "(":
            closure.insert(0, ")")
        elif line[i] == "[":
            closure.insert(0, "]")
        elif line[i] == "{":
            closure.insert(0, "}")
        elif line[i] == "<":
            closure.insert(0, ">")
        elif line[i] == ")":
            if closure[0] == ")":
                closure.pop(0)
            else:
                return scores[")"]
        elif line[i] == "]":
            if closure[0] == "]":
                closure.pop(0)
            else:
                return scores["]"]
        elif line[i] == "}":
            if closure[0] == "}":
                closure.pop(0)
            else:
                return scores["}"]
        elif line[i] == ">":
            if closure[0] == ">":
                closure.pop(0)
            else:
                return scores[">"]
    return 0


def line_checker_pt2(line):

    scores = {
        ")": 1,
        "]": 2,
        "}": 3,
        ">": 4,
    }

    closure = []

    for i in range(len(line)):

        if line[i] == "(":
            closure.insert(0, ")")
        elif line[i] == "[":
            closure.insert(0, "]")
        elif line[i] == "{":
            closure.insert(0, "}")
        elif line[i] == "<":
            closure.insert(0, ">")
        elif line[i] == closure[0]:
            closure.pop(0)
        elif i < len(line) - 1:
            return 0

    score = 0

    for j in range(len(closure)):
        score *= 5
        score += scores[closure[j]]

    return score


def part_1(value_list):

    score = 0

    for i in range(len(value_list)):
        score += line_checker(value_list[i])

    return score


def part_2(value_list):

    score = []

    for i in range(len(value_list)):
        result = line_checker_pt2(value_list[i])
        if result > 0:
            score.append(result)

    score.sort()

    return score[len(score) // 2]


if __name__ == '__main__':
    dir_path = os.path.dirname(os.path.realpath(__file__))

    input_read = read_file(dir_path + "/" + "input1.txt", "\n")

    value_list = input_read

    start_time = time.time()
    print("part 1: ", part_1(value_list))
    print("--- %s seconds ---" % (time.time() - start_time), "\n")

    start_time = time.time()
    print("part 2: ", part_2(value_list))
    print("--- %s seconds ---" % (time.time() - start_time), "\n")
