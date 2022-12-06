with open('input5.txt') as file:
    input = file.read().splitlines()    # open without /n

instructions = [line.replace('move ', '').split(' ') for line in input]
quantities = [int(instruction[0]) for instruction in instructions]
origins = [int(instruction[2]) - 1 for instruction in instructions]
destinations = [int(instruction[4]) - 1 for instruction in instructions]


def get_initialised_stacks(example):
    example_stacks = [['Z', 'N'], ['M', 'C', 'D'], ['P']]
    puzzle_stacks = [['R', 'G', 'J', 'B', 'T', 'V', 'Z'],
                     ['J', 'R', 'V', 'L'],
                     ['S', 'Q', 'F'],
                     ['Z', 'H', 'N', 'L', 'F', 'V', 'Q', 'G'],
                     ['R', 'Q', 'T', 'J', 'C', 'S', 'M', 'W'],
                     ['S', 'W', 'T', 'C', 'H', 'F'],
                     ['D', 'Z', 'C', 'V', 'F', 'N', 'J'],
                     ['L', 'G', 'Z', 'D', 'W', 'R', 'F', 'Q'],
                     ['J', 'B', 'W', 'V', 'P']]
    return example_stacks if example else puzzle_stacks


def puzzle1(stacks):
    for i in range(len(instructions)):
        for quantity in range(quantities[i]):
            crate = stacks[origins[i]].pop()
            stacks[destinations[i]].append(crate)

    crates = [stack.pop() for stack in stacks]
    print(''.join(crates))


def puzzle2(stacks):
    for i in range(len(instructions)):
        crates_to_move = [stacks[origins[i]].pop() for _ in range(quantities[i])]
        [stacks[destinations[i]].append(crates_to_move.pop()) for _ in range(quantities[i])]

    crates = [stack.pop() for stack in stacks]
    print(''.join(crates))


puzzle1(get_initialised_stacks(False))
puzzle2(get_initialised_stacks(False))
