import math
import os
import time

from utility.file_reader import read_file

position_value = {
    'E': 0,
    'S': 90,
    'W': 180,
    'N': 270,
}


def part_1(value_list, val=None, position='E'):
    if val is None:
        val = {
            'LAT': 0,
            'LON': 0
        }

    if len(value_list) == 0:
        return abs(val['LAT']) + abs(val['LON'])

    to_check = value_list[0]

    if to_check[:1] == 'L':
        new_val = position_value[position] - int(to_check[1:])
        # print(position, position_value[position], int(to_check[1:]), new_val)
        if new_val < 0:
            new_val = new_val + 360
        position = list(position_value.keys())[list(position_value.values()).index(new_val)]  # Prints george
        return part_1(value_list[1:], val, position)
    elif to_check[:1] == 'R':
        new_val = position_value[position] + int(to_check[1:])
        if new_val >= 360:
            new_val = new_val - 360
        position = list(position_value.keys())[list(position_value.values()).index(new_val)]  # Prints george
        return part_1(value_list[1:], val, position)

    if to_check[:1] == 'F':
        to_check = position + to_check[1:]

    if to_check[:1] == 'N':
        val['LON'] -= int(to_check[1:])
    elif to_check[:1] == 'S':
        val['LON'] += int(to_check[1:])
    elif to_check[:1] == 'E':
        val['LAT'] -= int(to_check[1:])
    elif to_check[:1] == 'W':
        val['LAT'] += int(to_check[1:])

    return part_1(value_list[1:], val, position)


def part_2(value_list, val=None, waypoint=None, position='E'):
    if val is None:
        val = {
            'LAT': 0,
            'LON': 0
        }

    if waypoint is None:
        waypoint = {
            'LAT': -10,
            'LON': -1
        }

    if len(value_list) == 0:
        return abs(val['LAT']) + abs(val['LON'])

    to_check = value_list[0]

    if to_check[:1] == 'L':
        new_val = position_value[position] - int(to_check[1:])
        if new_val < 0:
            new_val = new_val + 360
        position = list(position_value.keys())[list(position_value.values()).index(new_val)]
    elif to_check[:1] == 'R':
        new_val = position_value[position] + int(to_check[1:])
        if new_val >= 360:
            new_val = new_val - 360
        position = list(position_value.keys())[list(position_value.values()).index(new_val)]
    elif to_check[:1] == 'F':
        times = int(to_check[1:])

        if position == 'E':
            val['LON'] += waypoint['LON'] * times
            val['LAT'] += waypoint['LAT'] * times
        elif position == 'W':
            val['LON'] -= waypoint['LON'] * times
            val['LAT'] -= waypoint['LAT'] * times
        elif position == 'N':
            val['LON'] += waypoint['LAT'] * times
            val['LAT'] += waypoint['LON'] * times
        elif position == 'S':
            val['LON'] -= waypoint['LAT'] * times
            val['LAT'] -= waypoint['LON'] * times

    elif to_check[:1] == 'N':
        waypoint['LON'] -= int(to_check[1:])
    elif to_check[:1] == 'S':
        waypoint['LON'] += int(to_check[1:])
    elif to_check[:1] == 'E':
        waypoint['LAT'] -= int(to_check[1:])
    elif to_check[:1] == 'W':
        waypoint['LAT'] += int(to_check[1:])

    return part_2(value_list[1:], val, waypoint, position)


if __name__ == '__main__':
    dir_path = os.path.dirname(os.path.realpath(__file__))

    input_read = read_file(dir_path + "/" + "input1.txt")

    start_time = time.time()
    print('part 1:', part_1(input_read))
    print("--- %s seconds ---" % (time.time() - start_time), "\n")

    start_time = time.time()
    print('part 2:', part_2(input_read))
    print("--- %s seconds ---" % (time.time() - start_time), "\n")
