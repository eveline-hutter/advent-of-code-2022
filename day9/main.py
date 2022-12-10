with open('input9.txt') as file:
    input = file.read().splitlines()    # open without /n

instructions = [line.split(' ') for line in input]
directions = [instruction[0] for instruction in instructions]
no_of_steps = [int(instruction[1]) for instruction in instructions]


def move_head(moving_dir, head_pos):
    if moving_dir == 'R':
        head_pos[1] += 1
    elif moving_dir == 'L':
        head_pos[1] -= 1
    elif moving_dir == 'D':
        head_pos[0] += 1
    else:
        head_pos[0] -= 1
    return head_pos


def move_tail(head_pos, tail_pos):
    head_x, head_y, tail_x, tail_y = head_pos[0], head_pos[1], tail_pos[0], tail_pos[1]
    horizontal_distance = abs(head_y - tail_y)
    vertical_distance = abs(head_x - tail_x)
    if horizontal_distance > 1:
        tail_pos[1] = tail_y + 1 if head_y > tail_y else tail_y - 1
        if vertical_distance > 0:
            tail_pos[0] = tail_x + 1 if head_x > tail_x else tail_x - 1
        return tail_pos
    elif vertical_distance > 1:
        tail_pos[0] = tail_x + 1 if head_x > tail_x else tail_x - 1
        if horizontal_distance > 0:
            tail_pos[1] = tail_y + 1 if head_y > tail_y else tail_y - 1
        return tail_pos
    return False


def puzzle1():
    head_visited_positions = [[0, 0]]
    tail_visited_positions = [[0, 0]]

    for i in range(len(instructions)):
        direction = directions[i]
        for j in range(no_of_steps[i]):
            head_pos = move_head(direction, head_visited_positions[-1].copy())
            head_visited_positions.append(head_pos)
            tail_pos = move_tail(head_visited_positions[-1], tail_visited_positions[-1].copy())
            tail_visited_positions.append(tail_pos) if tail_pos else None

    different_positions = (set(tuple(pos) for pos in tail_visited_positions))
    print('no of visited positions by tail:', len(different_positions))


def puzzle2():
    heads_visited_positions = [[[0, 0]], [[0, 0]], [[0, 0]], [[0, 0]], [[0, 0]], [[0, 0]], [[0, 0]], [[0, 0]], [[0, 0]]]
    tails_visited_positions = [[[0, 0]], [[0, 0]], [[0, 0]], [[0, 0]], [[0, 0]], [[0, 0]], [[0, 0]], [[0, 0]], [[0, 0]]]

    for i in range(len(instructions)):
        direction = directions[i]
        for j in range(no_of_steps[i]):
            head_pos = move_head(direction, heads_visited_positions[0][-1].copy())
            heads_visited_positions[0].append(head_pos)
            for k in range(9):
                tail_pos = move_tail(heads_visited_positions[k][-1], tails_visited_positions[k][-1].copy())
                if tail_pos:
                    tails_visited_positions[k].append(tail_pos)
                    heads_visited_positions[k+1].append(tail_pos) if k < 8 else None
                else:
                    break

    different_positions = (set(tuple(pos) for pos in tails_visited_positions[-1]))
    print('no of visited positions by tail:', len(different_positions))


puzzle1()
puzzle2()
