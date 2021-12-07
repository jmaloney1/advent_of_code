import math

if __name__ == '__main__':

    with open('input') as f:
        diagnostic_map = list(map(lambda line: int(line.strip(), 2), f))

        max_row = int(max(map(math.log2, diagnostic_map)))
        print(diagnostic_map)

        def get_for_digit(i, digit):
            return min(1, i & int(math.pow(2, digit)))

        d_map = diagnostic_map
        for d in range(max_row, -1, -1):

            if len(d_map) == 1:
                print(d_map)
                break

            ones = list(filter(lambda i: get_for_digit(i, d) == 1, d_map))
            zeroes = list(filter(lambda i: get_for_digit(i, d) == 0, d_map))

            if len(ones) >= len(zeroes):
                d_map = ones
            else:
                d_map = zeroes

        oxygen_generator_rating = d_map[0]
        print(oxygen_generator_rating)

        d_map = diagnostic_map
        for d in range(max_row, -1, -1):

            if len(d_map) == 1:
                print(d_map)
                break

            ones = list(filter(lambda i: get_for_digit(i, d) == 1, d_map))
            zeroes = list(filter(lambda i: get_for_digit(i, d) == 0, d_map))

            if len(ones) < len(zeroes):
                d_map = ones
            else:
                d_map = zeroes

        co2_scrubbing_rating = d_map[0]
        print(co2_scrubbing_rating)

        print(oxygen_generator_rating * co2_scrubbing_rating)
