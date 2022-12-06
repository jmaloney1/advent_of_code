import util

if __name__ == '__main__':
    line = util.read_input('input')[0].strip()
    for i in range(0, len(line) - 13):
        buf = line[i: i + 14]
        print(f"{i}: {buf}")
        if len(set(buf)) == 14:
            print(i + 14)
            break
