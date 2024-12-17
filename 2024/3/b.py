import re
def main():
    with open("3/input/test") as f:
        line = f.read().strip()

    do_mul = True
    i = 0
    sum_mul = 0
    while i < len(line):
        next_dont = line[i:].find("don't()")
        next_do = line[i:].find("do()")
        if do_mul:
            regex = re.compile(r"mul\((\d+),(\d+)\)")

            if next_dont != -1:
                result = regex.findall(line[i:i+next_dont])
                for x, y in result:
                    sum_mul += int(x) * int(y)
            else:
                result = regex.findall(line[i:])
                break

            i = next_dont + 1
            do_mul = False
        
        elif not do_mul and next_do != -1:
            i = next_do + 1
            do_mul = True

    print(sum_mul)




if __name__ == "__main__":
    main()