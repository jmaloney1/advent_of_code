def sum_up_to(i):
    return int((i * (i+1)) / 2)


global m
if __name__ == '__main__':

    with open('input') as f:
        crabs = list(map(int, f.readline().strip().split(',')))
        m = 1234567889
        for i in range(min(crabs), max(crabs) + 1):
            m = min(sum(map(lambda x: sum_up_to(abs(x-i)), crabs)), m)

        print(m)
