import numpy as np

with open('input10.txt') as file:
    input = file.read().splitlines()    # read without /n


def puzzle1():
    regX = 1
    cycle = 0
    signal_strengths = []

    def check_for_interesting_signal():
        cycles = [20, 60, 100, 140, 180, 220]
        if cycle in cycles:
            signal_strengths.append(cycle * regX)

    for instruction in input:
        cycle += 1
        check_for_interesting_signal()
        if instruction[0] == 'a':
            cycle += 1
            check_for_interesting_signal()
            value = int(instruction.split(' ')[1])
            regX += value

    print('sum of interesting signal strengths:', sum(signal_strengths))


def puzzle2():
    regX = 1
    cycle = 0
    pixels = np.zeros((1, 240), dtype=str)

    def check_sprite():
        sprite = [regX - 1, regX, regX + 1]
        pixels[0][cycle] = '#' if ((cycle + 40) % 40) in sprite else '.'

    for instruction in input:
        check_sprite()
        cycle += 1
        if instruction[0] == 'a':
            check_sprite()
            cycle += 1
            value = int(instruction.split(' ')[1])
            regX += value

    pixels = pixels.reshape((6, 40))
    np.set_printoptions(linewidth=200)  # by default, only a portion of the screen width is used
    print(pixels)


puzzle1()
puzzle2()
