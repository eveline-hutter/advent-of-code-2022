with open('input6.txt') as file:
    input = file.read().splitlines()    # read without /n


def puzzle1():
    for datastream in input:
        for i in range(len(datastream) - 4):
            subdata = datastream[i:i+4]
            letter_counts = [subdata.count(subdata[j]) for j in range(3)]
            if sum(letter_counts) == 3:
                print('start-of-packet marker found at position', i + 4)
                break


def puzzle2():
    for datastream in input:
        for i in range(len(datastream) - 14):
            subdata = datastream[i:i+14]
            letter_counts = [subdata.count(subdata[j]) for j in range(13)]
            if sum(letter_counts) == 13:
                print('start-of-message marker found at position', i + 14)
                break


puzzle1()
puzzle2()
