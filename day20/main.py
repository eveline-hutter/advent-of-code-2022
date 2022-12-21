from collections import deque

with open('input20.txt') as file:
    puzzle_input = [int(line) for line in file.read().splitlines()]

file_length = len(puzzle_input)


def mix_numbers(input_values, coordinates, current_indices, no_of_times):
    for _ in range(no_of_times):
        # move the number in the order they originally appear in the encrypted file
        for i, val in enumerate(input_values):
            old_position = current_indices.index(i)
            del coordinates[old_position]
            del current_indices[old_position]
            coordinates.rotate(val * - 1)
            current_indices.rotate(val * -1)
            coordinates.insert(old_position, val)
            current_indices.insert(old_position, i)
    val_zero_position = coordinates.index(0)
    position_1000 = (1000 + val_zero_position) % file_length
    position_2000 = (2000 + val_zero_position) % file_length
    position_3000 = (3000 + val_zero_position) % file_length

    grove_coordinates = [coordinates[position_1000], coordinates[position_2000], coordinates[position_3000]]
    print('grove coordinates:', sum(grove_coordinates))


def puzzle1():
    coordinates = deque(puzzle_input.copy())
    current_index_list = deque([i for i in range(file_length)])
    mix_numbers(puzzle_input, coordinates, current_index_list, 1)


def puzzle2():
    decryption_key = 811589153
    new_puzzle_input = [value * decryption_key for value in puzzle_input]
    coordinates = deque(new_puzzle_input.copy())
    current_index_list = deque([i for i in range(file_length)])
    mix_numbers(new_puzzle_input, coordinates, current_index_list, 10)


puzzle1()
puzzle2()
