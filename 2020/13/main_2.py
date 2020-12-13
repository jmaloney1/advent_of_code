import math


def calculate_depart(timestamp, b):
    m = math.ceil(timestamp / b)
    return b * m


if __name__ == '__main__':
    with open('input', 'r') as input:
        input_list = [line.strip() for line in input]

    bus_cadences = [i for i in input_list[1].split(',')]
    buses = [(int(bus), i) for i, bus in enumerate(bus_cadences) if bus != 'x']
    buses.sort(key=lambda x: x[0], reverse=True)

    t = buses[0][0]
    step = 1
    for bus in buses:
        print(bus)
        while (t + bus[1]) % bus[0] != 0:
            t += step

        print(t)
        step *= bus[0]

    print(t)
