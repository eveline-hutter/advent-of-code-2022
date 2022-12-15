import numpy as np

with open('input14.txt') as file:
    input = file.read().splitlines()    # open without /n

paths = [line.split(' -> ') for line in input]

# draw cave outline
min_x, max_x = 0, 0
min_y, max_y = 500, 500

for i in range(len(paths)):
    points = []
    for point in paths[i]:
        coordinates = point.split(',')
        point_x, point_y = int(coordinates[1]), int(coordinates[0])
        points.append([point_x, point_y])
        min_x, max_x = min(point_x, min_x), max(point_x, max_x)
        min_y, max_y = min(point_y, min_y), max(point_y, max_y)
    paths[i] = points

cave_length_x, cave_length_y = max_x - min_x + 1, max_y - min_y + 1
cave = np.zeros((1000, 1000), dtype=str)


def get_stones_in_rock_path(stone1, stone2):
    # note that x and y are vice versa to the example
    min_x, max_x = min(stone1[0], stone2[0]), max(stone1[0], stone2[0])
    min_y, max_y = min(stone1[1], stone2[1]), max(stone1[1], stone2[1])
    x_diff, y_diff = abs(max_x - min_x), abs(max_y - min_y)

    stones_in_rock_path = []

    # get horizontal line
    if y_diff != 0:
        for i in range(min_y, max_y + 1):
            stones_in_rock_path.append([min_x, i])
    else:
        # get vertical line
        for i in range(min_x, max_x + 1):
            stones_in_rock_path.append([i, min_y])

    return stones_in_rock_path


# draw inside of cave
sand_source = [0, 500]
cave[sand_source[0]][sand_source[1]] = '+'

for path in paths:
    rock_structure = []
    for point in path:
        rock_structure.append([point[0], point[1]])

    for i in range(len(rock_structure) - 1):
        stones = get_stones_in_rock_path(rock_structure[i], rock_structure[i + 1])

        for stone in stones:
            cave[stone[0]][stone[1]] = '#'

cave_copy = cave.copy()


def let_sand_fall_recursively(sand_unit, local_cave):
    x, y = sand_unit[0], sand_unit[1]
    if x + 1 > max_x + 2:
        return False
    if local_cave[x + 1][y] == '':
        return let_sand_fall_recursively([x + 1, y], local_cave)
    elif local_cave[x + 1][y - 1] == '':
        return let_sand_fall_recursively([x + 1, y - 1], local_cave)
    elif local_cave[x + 1][y + 1] == '':
        return let_sand_fall_recursively([x + 1, y + 1], local_cave)
    else:
        return [x, y]


def puzzle1():
    falling_into_the_endless_void = False
    while not falling_into_the_endless_void:
        sand_coordinates = let_sand_fall_recursively(sand_source, cave)
        if not sand_coordinates:
            falling_into_the_endless_void = True
        else:
            cave[sand_coordinates[0]][sand_coordinates[1]] = 'o'
    no_of_sand_units = np.count_nonzero(cave == 'o')
    print('number of sand units before sand starts flowing into the abyss below:', no_of_sand_units)


def puzzle2():
    cave_copy[max_x + 2] = '#'
    blocking_the_source = False
    counter = 0
    while not blocking_the_source:
        counter += 1
        sand_coordinates = let_sand_fall_recursively(sand_source, cave_copy)
        if sand_coordinates == [0, 500]:
            blocking_the_source = True
        else:
            cave_copy[sand_coordinates[0]][sand_coordinates[1]] = 'o'

    no_of_sand_units = np.count_nonzero(cave_copy == 'o')
    print('number of sand units coming to rest:', no_of_sand_units + 1)     # plus 1 for the unit on the sand source


puzzle1()
puzzle2()
