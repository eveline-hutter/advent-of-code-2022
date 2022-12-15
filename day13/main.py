import ast

with open('input13.txt') as file:
    input = file.read().splitlines()  # open without /n


def check_order(left, right):
    for i in range(max(len(left), len(right))):
        # check if either side is empty
        left_empty, right_empty = len(left) <= i, len(right) <= i
        if left_empty:
            return True
        if right_empty:
            return False

        first, second = left[i], right[i]
        comparison = False

        # check if types differ
        if type(first) == int:
            if type(second) == int:
                if first < second:
                    comparison = True
                elif first > second:
                    comparison = False
            else:
                first = [first]
                comparison = check_order(first, second)
        else:
            if type(second) == int:
                second = [second]
                comparison = check_order(first, second)
            else:
                comparison = check_order(first, second)

        return comparison


def puzzle1():
    packet_pairs = [[ast.literal_eval(input[i]), ast.literal_eval(input[i + 1])] for i in range(0, len(input), 3)]

    pairs_in_correct_order = []

    for i in range(len(packet_pairs)):
        correct_order = check_order(packet_pairs[i][0], packet_pairs[i][1])
        if correct_order:
            pairs_in_correct_order.append(i + 1)

    print('sum of indices of packet pairs in correct order:', sum(pairs_in_correct_order))


def puzzle2():

    packets = [ast.literal_eval(input[i]) for i in range(len(input)) if input[i] != '']

    # # get the position of the divider packets
    first_divider_packet, second_divider_packet = [[2]], [[6]]
    position_of_first_divider_packet = 1
    position_of_second_divider_packet = 2

    for packet in packets:
        if check_order(packet, first_divider_packet):
            position_of_first_divider_packet += 1
        if check_order(packet, second_divider_packet):
            position_of_second_divider_packet += 1

    print('decoder key for distress signal:', position_of_first_divider_packet * position_of_second_divider_packet)


puzzle1()
puzzle2()
