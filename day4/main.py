import math
import numbers
import os
import re
import sys
import time

from utility.file_reader import read_file


def part_1(value_list, valid=0):
    if len(value_list) == 0:
        return valid

    passport = value_list[0].split()

    fields = {
        'byr',
        'iyr',
        'eyr',
        'hgt',
        'hcl',
        'ecl',
        'pid',
    }

    passport_dict = {passport[i][0:3]: passport[i][4:] for i in range(0, len(passport))}

    if all(k in passport_dict for k in fields):
        return part_1(value_list[1:], valid + 1)
    else:
        return part_1(value_list[1:], valid)


def number_range_validation(val, lenght, val_range):
    return val.isnumeric() and len(val) == lenght and val_range[0] <= int(val) <= val_range[1]


def hgt_validation(val):
    if val[-2:] == 'cm':
        return number_range_validation(val[:-2], 3, [150, 193])
    elif val[-2:] == 'in':
        return number_range_validation(val[:-2], 2, [59, 76])
    else:
        return False


def part_2(value_list, valid=0, ):
    if len(value_list) == 0:
        return valid

    passport = value_list[0].split()

    fields = {
        'byr',
        'iyr',
        'eyr',
        'hgt',
        'hcl',
        'ecl',
        'pid',
    }

    validation = {
        'byr': lambda x: number_range_validation(x, 4, [1920, 2002]),
        'iyr': lambda x: number_range_validation(x, 4, [2010, 2020]),
        'eyr': lambda x: number_range_validation(x, 4, [2020, 2030]),
        'hgt': lambda x: hgt_validation(x),
        'hcl': lambda x: x[0] == '#' and len(x[1:]) == 6 and re.match("^[a-f0-9]*$", x[1:]),
        'ecl': lambda x: x == 'amb' or x == 'blu' or x == 'brn' or x == 'gry' or x == 'grn' or x == 'hzl' or x == 'oth',
        'pid': lambda x: number_range_validation(x, 9, [0, sys.maxsize]),
        'cid': lambda x: 1 == 1
    }

    passport_dict = {passport[i][0:3]: passport[i][4:] for i in range(0, len(passport))}

    if all(k in passport_dict for k in fields) and all(
            validation.get(k, lambda x: False)(v) for (k, v) in passport_dict.items()):
        return part_2(value_list[1:], valid + 1)
    else:
        return part_2(value_list[1:], valid)


if __name__ == '__main__':
    dir_path = os.path.dirname(os.path.realpath(__file__))

    input_read = read_file(dir_path + "/" + "input1.txt", "\n\n")

    start_time = time.time()
    print('part 1:', part_1(input_read))
    print("--- %s seconds ---" % (time.time() - start_time), "\n")

    start_time = time.time()
    print('part 2:', part_2(input_read))
    print("--- %s seconds ---" % (time.time() - start_time), "\n")
