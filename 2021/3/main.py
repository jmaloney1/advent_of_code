if __name__ == '__main__':

    with open('input') as f:
        diagnostic_map = list(map(lambda line: list(map(lambda i: int(i), line.strip())), f))
        print(diagnostic_map)

        diagnostic_map_inv = [[n[i] for n in diagnostic_map] for i in range(len(diagnostic_map[0]))]

        c0 = [0 if row.count(0) > len(diagnostic_map_inv[0])/2 else 1 for row in diagnostic_map_inv]
        c1 = [0 if row.count(1) > len(diagnostic_map_inv[0])/2 else 1 for row in diagnostic_map_inv]
        print(diagnostic_map_inv)
        gamma_rate = int(''.join(map(lambda s: str(s), c0)), 2)
        epsilon_rate = int(''.join(map(lambda s: str(s), c1)), 2)
        print(gamma_rate)
        print(epsilon_rate)
        print(gamma_rate * epsilon_rate)
