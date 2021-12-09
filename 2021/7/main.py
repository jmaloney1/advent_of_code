if __name__ == '__main__':

    with open('input') as f:
        crabs = list(map(int, f.readline().strip().split(',')))
        m = 1234567889
        for i in range(min(crabs), max(crabs) + 1):
            m = min(sum(map(lambda x: abs(x-i), crabs)), m)

        print(m)
