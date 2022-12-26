with open('input25.txt') as file:
    puzzle_input = file.read().splitlines()  # open without /n


def get_digit(snafu_digit):
    switch = {
        '2': 2,
        '1': 1,
        '0': 0,
        '-': -1,
        '=': -2
        }
    return switch.get(snafu_digit, "unknown snafu digit")


def snafu_to_decimal(snafu_nr):
    dec_no = 0
    for i in range(len(snafu_nr)):
        digit = get_digit(snafu_nr[-1 - i])
        dec_no += digit * 5**i
    return dec_no


sum_decimals = sum([snafu_to_decimal(number) for number in puzzle_input])
