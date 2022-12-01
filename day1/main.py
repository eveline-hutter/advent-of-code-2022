with open('input1.txt') as file:
    input = file.read().splitlines()  # open without /n


def puzzle1():
    elves_calories = []
    calories = 0

    for cal in input:
        if cal == '':
            elves_calories.append(calories)
            calories = 0
        else:
            calories += int(cal)

    return elves_calories


def puzzle2(elves_calories):
    sorted_elves_calories = sorted(elves_calories, reverse=True)
    print('puzzle2:', sum(sorted_elves_calories[:3]))


elves_calories = puzzle1()
print('puzzle1:', max(elves_calories))
puzzle2(elves_calories)
