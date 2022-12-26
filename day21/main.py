from sympy import *

with open('input21.txt') as file:
    puzzle_input = file.read().splitlines()

identified_numbers = []
unidentified_numbers = []

for yell in puzzle_input:
    yell = yell.split(': ')
    if yell[0] == 'humn':
        identified_numbers.append([yell[0], Symbol('x')])
    else:
        try:
            identified_numbers.append([yell[0], int(yell[1])])
        except ValueError:
            result = yell[1].split(' ')
            unidentified_numbers.append([yell[0], result])


def get_number(monkey):
    for identified_number in identified_numbers:
        if identified_number[0] == monkey:
            return identified_number[1]


def get_result(first_number, second_number, operator):
    if operator == '+':
        return first_number + second_number
    elif operator == '-':
        return first_number - second_number
    elif operator == '*':
        return first_number * second_number
    else:
        return first_number // second_number


while len(unidentified_numbers) > 0:
    for yell in unidentified_numbers:
        monkey = yell[0]
        number = yell[1]
        # test if both numbers of the operation are already identified
        first_no = get_number(number[0])
        if first_no is not None:
            second_no = get_number(number[2])
            if second_no is not None:
                operator = number[1]
                result = get_result(first_no, second_no, operator)
                unidentified_numbers.remove(yell)
                identified_numbers.append([monkey, result])

root_result = identified_numbers[-1][1]
print('monkey named root yells:', root_result)
x = Symbol('x')
str_result = str(root_result).replace('floor', '').replace(' ', '')
last_plus = 0
for i in range(len(str_result) - 1, 0, -1):
    if str_result[i] == '+':
        last_plus = i
        break
str_equation = ''
for i in range(len(str_result)):
    str_equation += '-' if i == last_plus else str_result[i]
sym_result = sympify(str_equation)
result = solve(sym_result)
print(result)
