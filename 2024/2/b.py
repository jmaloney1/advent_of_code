def main():
    with open("2/input/input") as f:
        lines = [list(map(int, line.strip().split())) for line in f.readlines()]

    print(lines)

    def inc_safe(line):
        for i in range(len(line) - 1):
            x, y = line[i:i+2]
            if not (x < y and y - x <= 3):
                return False
        return True
    
    def dec_safe(line):
        for i in range(len(line) - 1):
            x, y = line[i:i+2]
            if not (x > y and x - y <= 3):
                return False
        return True

    safe_count = 0
    for line in lines:
        if inc_safe(line):
            safe_count += 1
        elif dec_safe(line):
            safe_count += 1
        else:
            for i in range(len(line)):
                new_line = line[:i] + line[i+1:]
                if inc_safe(new_line):
                    safe_count += 1
                    break
                elif dec_safe(new_line):
                    safe_count += 1
                    break
    print(safe_count)






if __name__ == "__main__":
    main()