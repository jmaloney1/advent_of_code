if __name__ == '__main__':
    with open('test_input') as f:
        height_map = [l.strip() for l in f]

        for x in height_map:
            for i in range(len(x)):
                w = x[max(0, i-1):min(len(x), i+2)]

                if i == 0:

                print(w)

        print(height_map)