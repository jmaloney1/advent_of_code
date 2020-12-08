import sys
import math

def main():
    wire_1 = list(map(lambda s: (s[0], int(s[1:])), sys.stdin.readline().split(',')))
    wire_2 = list(map(lambda s: (s[0], int(s[1:])), sys.stdin.readline().split(',')))

    #print(f"Input: {wire_1}")
    #print(f"Input: {wire_2}")

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
    intersections = []
    for i in wire_2:
        if i[0] == 'L':
            for x in range(x_2, x_2 - i[1], -1):
                if (x, y_2) in wire_1_points:
                    intersections.append((x, y_2))
            x_2 = x_2 - i[1]
        elif i[0] == 'R':
            for x in range(x_2, x_2 + i[1]):
                if (x, y_2) in wire_1_points:
                    intersections.append((x, y_2))
            x_2 = x_2 + i[1]
        elif i[0] == 'U':
            for y in range(y_2, y_2 + i[1]):
                if (x_2, y) in wire_1_points:
                    intersections.append((x_2, y))
            y_2 = y_2 + i[1]
        elif i[0] == 'D':
            for y in range(y_2, y_2 - i[1], -1):
                if (x_2, y) in wire_1_points:
                    intersections.append((x_2, y))
            y_2 = y_2 - i[1]

    #print(f"Position of wire 2: ({x_2}, {y_2})")

    cur_min = 10000000
    intersection = None
    for i in intersections:
        man = abs(i[0]) + abs(i[1])
        print(f"Intersection at: {i}. Manhattan distance of: {man}")
        if cur_min > man:
            cur_min = man
            intersection = i

    print(f"Max Manhattan: {cur_min}")

if __name__ == '__main__':
    main()

