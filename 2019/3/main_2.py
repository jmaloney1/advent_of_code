import sys
import math

def main():
    wire_1 = list(map(lambda s: (s[0], int(s[1:])), sys.stdin.readline().split(',')))
    wire_2 = list(map(lambda s: (s[0], int(s[1:])), sys.stdin.readline().split(',')))

    #print(f"Input: {wire_1}")
    #print(f"Input: {wire_2}")

    intersections = get_intersections(wire_1, wire_2)

    distance_map_1 = get_distances(wire_1, intersections)
    distance_map_2 = get_distances(wire_2, intersections)

    print(f"Distance map 1: {distance_map_1}")
    print(f"Distance map 2: {distance_map_2}")

    min_dist = 100000000000
    for i in intersections:
        dist = distance_map_1[i] + distance_map_2[i]
        print(f"Distance for intersection {i}: {dist}")
        if dist < min_dist:
            min_dist = dist

    print(f"Minimum distance to intersection: {min_dist}")


def get_distances(wire, intersections):
    x_1 = 0
    y_1 = 0
    distance_map = dict()
    dist = 0
    for i in wire:
        if i[0] == 'L':
            for x in range(x_1, x_1 - i[1], -1):
                if (x, y_1) in intersections:
                    distance_map[(x, y_1)] = dist
                dist = dist + 1
            x_1 = x_1 - i[1]
        elif i[0] == 'R':
            for x in range(x_1, x_1 + i[1]):
                if (x, y_1) in intersections:
                    distance_map[(x, y_1)] = dist
                dist = dist + 1
            x_1 = x_1 + i[1]
        elif i[0] == 'U':
            for y in range(y_1, y_1 + i[1]):
                if (x_1, y) in intersections:
                    distance_map[(x_1, y)] = dist
                dist = dist + 1
            y_1 = y_1 + i[1]
        elif i[0] == 'D':
            for y in range(y_1, y_1 - i[1], -1):
                if (x_1, y) in intersections:
                    distance_map[(x_1, y)] = dist
                dist = dist + 1
            y_1 = y_1 - i[1]

    return distance_map


def get_intersections(wire_1, wire_2):
    x_1 = 0
    y_1 = 0
    wire_1_points = set()
    for i in wire_1:
        if i[0] == 'L':
            for x in range(x_1, x_1 - i[1], -1):
                wire_1_points.add((x, y_1))
            x_1 = x_1 - i[1]
        elif i[0] == 'R':
            for x in range(x_1, x_1 + i[1]):
                wire_1_points.add((x, y_1))
            x_1 = x_1 + i[1]
        elif i[0] == 'U':
            for y in range(y_1, y_1 + i[1]):
                wire_1_points.add((x_1, y))
            y_1 = y_1 + i[1]
        elif i[0] == 'D':
            for y in range(y_1, y_1 - i[1], -1):
                wire_1_points.add((x_1, y))
            y_1 = y_1 - i[1]

    wire_1_points.remove((0,0))

    #print(f"Position of wire 1: ({x_1}, {y_1})")
    #print(f"Points for wire 1: {wire_1_points}")

    x_2 = 0
    y_2 = 0
    intersections = set()
    for i in wire_2:
        if i[0] == 'L':
            for x in range(x_2, x_2 - i[1], -1):
                if (x, y_2) in wire_1_points:
                    intersections.add((x, y_2))
            x_2 = x_2 - i[1]
        elif i[0] == 'R':
            for x in range(x_2, x_2 + i[1]):
                if (x, y_2) in wire_1_points:
                    intersections.add((x, y_2))
            x_2 = x_2 + i[1]
        elif i[0] == 'U':
            for y in range(y_2, y_2 + i[1]):
                if (x_2, y) in wire_1_points:
                    intersections.add((x_2, y))
            y_2 = y_2 + i[1]
        elif i[0] == 'D':
            for y in range(y_2, y_2 - i[1], -1):
                if (x_2, y) in wire_1_points:
                    intersections.add((x_2, y))
            y_2 = y_2 - i[1]

    #print(f"Position of wire 2: ({x_2}, {y_2})")

    cur_min = 10000000
    intersection = None
    for i in intersections:
        man = abs(i[0]) + abs(i[1])
        #print(f"Intersection at: {i}. Manhattan distance of: {man}")
        if cur_min > man:
            cur_min = man
            intersection = i

    print(f"Max Manhattan: {cur_min}")

    return intersections


if __name__ == '__main__':
    main()

