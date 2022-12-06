import util

if __name__ == '__main__':
    line = util.read_input('input')[0].strip()
    for i in range(0, len(line) - 3):
        buf = line[i: i + 4]
        print(f"{i}: {buf}")
        if len(set(buf)) == 4:
            print(i + 4)
            break
