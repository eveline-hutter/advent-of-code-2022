import numpy as np

with open('input8.txt') as file:
    input = file.read().splitlines()    # open without /n

trees = [[int(tree) for tree in line] for line in input]


def puzzle1():
    visible_trees = np.zeros((len(trees), len(trees)), dtype=int)

    # all trees around the edge are visible
    for i in range(len(trees)):
        visible_trees[i][0] += 1
        visible_trees[i][-1] += 1
    for j in range(len(trees)):
        visible_trees[0][j] += 1
        visible_trees[-1][j] += 1

    # traverse from left
    for i in range(len(trees)):
        max_height = trees[i][0]
        for j in range(len(trees[i])):
            tree = trees[i][j]
            if tree > max_height:
                max_height = tree
                visible_trees[i][j] += 1

    # traverse from right
    for i in range(len(trees)):
        max_height = trees[i][-1]
        for j in range(len(trees[i]) - 1, -1, -1):
            tree = trees[i][j]
            if tree > max_height:
                max_height = tree
                visible_trees[i][j] += 1

    # traverse from top
    for j in range(len(trees[0])):
        max_height = trees[0][j]
        for i in range(len(trees)):
            tree = trees[i][j]
            if tree > max_height:
                max_height = tree
                visible_trees[i][j] += 1

    # traverse from bottom
    for j in range(len(trees[0])):
        max_height = trees[-1][j]
        for i in range(len(trees) - 1, -1, -1):
            tree = trees[i][j]
            if tree > max_height:
                max_height = tree
                visible_trees[i][j] += 1

    print('visible trees:', np.count_nonzero(visible_trees))


def puzzle2():
    scenic_scores = np.zeros((len(trees), len(trees[0])), dtype=int)

    for i in range(1, len(trees) - 1):
        for j in range(1, len(trees[0]) - 1):
            viewing_distances = np.zeros((1, 4))

            # looking right
            for k in range(j + 1, len(trees)):
                viewing_distances[0][0] += 1
                if trees[i][k] >= trees[i][j]:
                    break

            # looking left
            for k in range(j - 1, -1, -1):
                viewing_distances[0][1] += 1
                if trees[i][k] >= trees[i][j]:
                    break

            # looking down
            for m in range(i + 1, len(trees[0])):
                viewing_distances[0][2] += 1
                if trees[m][j] >= trees[i][j]:
                    break

            # looking down
            for m in range(i - 1, -1, -1):
                viewing_distances[0][3] += 1
                if trees[m][j] >= trees[i][j]:
                    break

            # set all zeros to ones to avoid multiplying by zero
            viewing_distances[viewing_distances == 0] = 1
            scenic_score = np.prod(viewing_distances)
            scenic_scores[i][j] = scenic_score

    print('highest scenic score:', np.max(scenic_scores))


puzzle1()
puzzle2()
