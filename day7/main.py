with open('input7.txt') as file:
    input = file.read().splitlines()    # open without /n

dirs = []   # per directory: index 0 = name, index 1 = parent, index 2 = depth, index 3 = content (size)
parent_dir_name = ''
curr_dir_name = ''
curr_dir_depth = 0

for i in range(len(input)):
    command = input[i].split(' ')
    if command[0] == '$':
        if command[1] == 'cd':
            if command[2] != '..':
                curr_dir_depth += 1
                parent_dir_name = curr_dir_name
                curr_dir_name += command[2]
                if i != 0:
                    curr_dir_name += '/'
                if not dirs.__contains__([curr_dir_name]):
                    dirs.append([curr_dir_name])
            else:
                curr_dir_depth -= 1
                curr_dir_index = -1
                for k in range(len(dirs)):
                    if dirs[k][0] == curr_dir_name:
                        curr_dir_index = k
                curr_dir = dirs[curr_dir_index]
                curr_dir_name = curr_dir[1]
                parent_dir_index = -1
                for l in range(len(dirs)):
                    if dirs[l][0] == curr_dir_name:
                        parent_dir_index = l
                parent_dir = dirs[parent_dir_index]
                parent_dir_name = parent_dir[1]
        else:   # ls
            dir_size = 0
            for j in range(i + 1, len(input)):
                content = input[j].split(' ')
                if content[0] == '$':
                    break
                else:
                    if content[0] != 'dir':
                        dir_size += int(content[0])
            curr_dir = dirs[dirs.index([curr_dir_name])]
            curr_dir.append(parent_dir_name)
            curr_dir.append(curr_dir_depth)
            curr_dir.append(dir_size)


def puzzle1():
    max_depth = max([directory[2] for directory in dirs])
    for depth in range(max_depth, 0, -1):
        for directory in dirs:
            if directory[2] == depth:
                if directory[1] != '':
                    parent_dir_index = -1
                    for l in range(len(dirs)):
                        if dirs[l][0] == directory[1]:
                            parent_dir_index = l
                    parent_dir = dirs[parent_dir_index]
                    parent_dir[3] += directory[3]

    print('total sizes sum of small directories:', sum([directory[3] for directory in dirs if directory[3] <= 100000]))


def puzzle2():
    unused_space = 70000000 - dirs[0][3]
    space_to_free_up = 30000000 - unused_space
    used_spaces = sorted([directory[3] for directory in dirs])
    for space in used_spaces:
        if space >= space_to_free_up:
            print('total size of directory to delete:', space)
            break


puzzle1()
puzzle2()
