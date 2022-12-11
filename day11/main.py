import math

with open('input11.txt') as file:
    input = file.read().splitlines()    # open without /n

input = [line.replace('  ', '') for line in input]


def initiate_monkeys():
    monkeys = []

    for i in range(0, len(input), 7):
        starting_items = input[i + 1].replace('Starting items: ', '').split(', ')
        operation = input[i + 2].replace('Operation: new = old ', '').split(' ')
        divide_by = int(input[i + 3].split(' ')[-1])
        monkey_true = int(input[i + 4].split(' ')[-1])
        monkey_false = int(input[i + 5].split(' ')[-1])
        monkeys.append([[int(item) for item in starting_items], operation, divide_by, monkey_true, monkey_false, 0])

    return monkeys


def calculate_worry_level(old_worry_lvl, operation):
    first = int(old_worry_lvl)
    second = int(old_worry_lvl) if operation[1] == 'old' else int(operation[1])
    return first * second if operation[0] == '*' else first + second


def throw_items(monkeys, rounds, relief):
    # calculate the least common multiple of all divisors for part 2
    least_common_multiple = 1
    for monkey in monkeys:
        least_common_multiple = math.lcm(least_common_multiple, monkey[2])

    for _ in range(rounds):
        for monkey in monkeys:
            for item in monkey[0]:
                monkey[5] += 1
                new_worry_level = calculate_worry_level(item, monkey[1])
                if relief:
                    new_worry_level = new_worry_level // 3
                else:
                    new_worry_level = new_worry_level % least_common_multiple
                test = (new_worry_level % monkey[2]) == 0
                if test:
                    monkeys[monkey[3]][0].append(new_worry_level)
                else:
                    monkeys[monkey[4]][0].append(new_worry_level)
                monkey[0] = []
    return monkeys


def puzzle1():
    monkeys = initiate_monkeys()
    monkeys = throw_items(monkeys, 20, True)
    no_of_inspections = sorted([monkey[5] for monkey in monkeys], reverse=True)
    print('monkey business after 20 rounds of stuff-slinging simian shenanigans:', math.prod(no_of_inspections[:2]))


def puzzle2():
    monkeys = initiate_monkeys()
    monkeys = throw_items(monkeys, 10000, False)
    no_of_inspections = sorted([monkey[5] for monkey in monkeys], reverse=True)
    print('monkey business after 10000 rounds of stuff-slinging simian shenanigans:', math.prod(no_of_inspections[:2]))


puzzle1()
puzzle2()
