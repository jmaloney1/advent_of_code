import re
def main():
    with open("3/input/input") as f:
        line = f.read().strip()

    regex = re.compile(r"mul\((\d+),(\d+)\)")

    result = regex.findall(line)

    for x, y in result:
        print(int(x) * int(y))

    print(sum(int(x) * int(y) for x, y in result))




if __name__ == "__main__":
    main()