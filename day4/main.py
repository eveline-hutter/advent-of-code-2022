import numpy as np

with open('input4.txt') as file:
    input = file.read().splitlines()    # open without /n

assignments = [line.split(',') for line in input]
first_assignments = [assignment[0].split('-') for assignment in assignments]
second_assignments = [assignment[1].split('-') for assignment in assignments]

first_elves = [np.arange(int(assignment[0]), int(assignment[1]) + 1) for assignment in first_assignments]
second_elves = [np.arange(int(assignment[0]), int(assignment[1]) + 1) for assignment in second_assignments]


def puzzle1():
    to_reconsider = 0

    for i in range(len(assignments)):
        first, second = set(first_elves[i]), set(second_elves[i])
        len_1, len_2 = len(first), len(second)
        comp = first.intersection(second)
        if len(comp) == len_1 or len(comp) == len_2:
            to_reconsider += 1

    print('to_reconsider:', to_reconsider, 'pairs')


def puzzle2():
    to_reconsider = 0

    for i in range(len(assignments)):
        first, second = set(first_elves[i]), set(second_elves[i])
        comp = first.intersection(second)
        if len(comp) > 0:
            to_reconsider += 1

    print('to reconsider:', to_reconsider, 'pairs')


puzzle1()
puzzle2()
