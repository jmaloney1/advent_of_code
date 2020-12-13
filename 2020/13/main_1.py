import math


def calculate_depart(timestamp, b):
    m = math.ceil(timestamp / b)
    return b * m


if __name__ == '__main__':
    with open('input', 'r') as input:
        input_list = [line.strip() for line in input]

    timestamp = int(input_list[0])
    bus_cadences = [int(i) for i in input_list[1].split(',') if i != 'x']

    departure_times = [(b, calculate_depart(timestamp, b)) for b in bus_cadences]

    min_dep = min(departure_times, key=lambda x: x[1])
    print(min_dep[0] * (min_dep[1] - timestamp))
