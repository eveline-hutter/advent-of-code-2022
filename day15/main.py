import numpy as np

np.set_printoptions(linewidth=200)  # by default, only a portion of the screen width is used

with open('input15.txt') as file:
    input = file.read().splitlines()    # open without /n

sensors = [line.split(': ')[0] for line in input]
beacons = [line.split(': ')[1] for line in input]

x_coordinates, y_coordinates = [], []

for i in range(len(sensors)):
    # note that x and y are vice versa to the example
    s = sensors[i].split(', ')
    s_y = int(s[0].replace('Sensor at x=', ''))
    s_x = int(s[1].replace('y=', ''))
    sensors[i] = [s_x, s_y]
    x_coordinates.append(s_x)
    y_coordinates.append(s_y)

    b = beacons[i].split(', ')
    b_y = int(b[0].replace('closest beacon is at x=', ''))
    b_x = int(b[1].replace('y=', ''))
    beacons[i] = [b_x, b_y]
    x_coordinates.append(b_x)
    y_coordinates.append(b_y)

min_x, max_x = min(x_coordinates), max(x_coordinates)
min_y, max_y = min(y_coordinates), max(y_coordinates)

height, width = max_x - min_x + 1, max_y - min_y + 1
area = np.zeros((height, width), dtype='uint8')

sensors = [[s[0] - min_x, s[1] - min_y] for s in sensors]
beacons = [[b[0] - min_x, b[1] - min_y] for b in beacons]


def calculate_distance(source, target):
    return abs(target[0] - source[0]) + abs(target[1] - source[1])


def get_signal_area(sensor):
    signal_area = np.zeros(area.shape, dtype='uint8')
    for i in range(len(signal_area)):
        for j in range(len(signal_area[i])):
            signal_area[i][j] = calculate_distance(sensor, [i, j])
    return signal_area


for i in range(len(sensors)):
    s, b = sensors[i], beacons[i]
    # add sensors to area
    area[s[0]][s[1]] = 5
    # add beacons to area
    area[b[0]][b[1]] = 8
    # calculate manhattan distance
    distance = calculate_distance(s, b)
    # add area where no beacon is present
    signal_area = get_signal_area(s)
    signal_area = signal_area <= distance
    for j in range(len(signal_area)):
        for k in range(len(signal_area[j])):
            if signal_area[j][k] and not area[j][k]:
                area[j][k] = 1

print('no of positions that cannot contain a beacon:', np.count_nonzero(area[10] == 1))
