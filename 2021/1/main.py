if __name__ == '__main__':

    with open('input') as f:
        prev = None
        c = 0
        window_size = 3
        ints = list(map(lambda i: int(i), f))
        for i, x in enumerate(ints):
            window = ints[i:i+window_size]
            print(window)

            if len(window) < window_size:
                break

            if prev is not None and prev < sum(window):
                c += 1
            prev = sum(window)

        print(c)
