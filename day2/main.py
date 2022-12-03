with open('input2.txt') as file:
    input = file.read().splitlines()  # open without /n


def puzzle1():
    def get_choice(letter):
        switch = {
            'A': 1,
            'X': 1,
            'B': 2,
            'Y': 2,
            'C': 3,
            'Z': 3
        }
        return switch.get(letter, "wrong input")

    def get_score(result):
        switch = {
            -1: 6,
            2: 6,
            0: 3
        }
        return switch.get(result, 0)

    opponent = [get_choice(round[0]) for round in input]
    player = [get_choice(round[2]) for round in input]
    scores = 0
    for round in range(len(input)):
        score = player[round]   # get first score from shape
        result = opponent[round] - player[round]
        score += get_score(result)
        scores += score
    print('Total score:', scores)


def puzzle2():
    opponent = [round[0] for round in input]
    result = [round[2] for round in input]

    def get_result(opponent_shape, wished_result):
        if opponent_shape == 'A':
            switch = {
                'X': 3,
                'Y': 4,
                'Z': 8
            }
            return switch.get(wished_result, 'wrong input')
        elif opponent_shape == 'B':
            switch = {
                'X': 1,
                'Y': 5,
                'Z': 9
            }
            return switch.get(wished_result, 'wrong input')
        else:
            switch = {
                'X': 2,
                'Y': 6,
                'Z': 7
            }
            return switch.get(wished_result, 'wrong input')

    scores = [get_result(opponent[round], result[round]) for round in range(len(input))]
    print('Total score:', sum(scores))

puzzle1()
puzzle2()
