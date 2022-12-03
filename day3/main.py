import difflib

with open('input3.txt') as file:
    input = file.read().splitlines()    # open without /n


def get_priority(item):
    # ASCII table starts A.Z at 65 and a.z at 97
    ascii_value = ord(item)
    return ascii_value - 96 if ascii_value >= 97 else ascii_value - 38


def puzzle1():
    first_compartment = [line[: (len(line) // 2)] for line in input]
    second_compartment = [line[len(line) // 2:] for line in input]

    wrong_items = [list((set(first_compartment[i]) & set(second_compartment[i])))[0] for i in range(len(input))]
    priorities = [get_priority(item) for item in wrong_items]
    print('sum of priorities', sum(priorities))


def puzzle2():
    groups = [[input[i], input[i+1], input[i+2]] for i in range(0, len(input), 3)]
    badges = [list(set(group[0]) & set(group[1]) & set(group[2]))[0] for group in groups]
    priorities = [get_priority(badge) for badge in badges]
    print('sum of priorities', sum(priorities))


puzzle1()
puzzle2()
