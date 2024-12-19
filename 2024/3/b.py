import re
import os
def main():
    os.chdir(os.path.dirname(os.path.realpath(__file__))) 

    with open("input/test") as f:
        line = f.read().strip()

    i = 0
    sum_mul = 0
    regex = re.compile(r"mul\((\d+),(\d+)\)")

    while i < len(line) and i >= 0:
        # Find next don't() relative to current position
        relative_dont = line[i:].find("don't()")
        next_dont = relative_dont + i if relative_dont != -1 else -1
        
        print(f"next_dont {next_dont} at {line[next_dont-2:next_dont+7] if next_dont != -1 else 'not found'}")
        
        if next_dont == -1:
            result = regex.findall(line[i:])
            for x, y in result:
                print(f"mul {x} {y}")
                sum_mul += int(x) * int(y)
            break
            
        result = regex.findall(line[i:next_dont])
        for x, y in result:
            print(f"mul {x} {y}")
            sum_mul += int(x) * int(y)
            
        # Find next do() relative to don't position
        relative_do = line[next_dont:].find("do()")
        i = next_dont + relative_do if relative_do != -1 else -1
        
        print(f"moving to next do() at {i} {line[i-2:i+5] if i != -1 else 'not found'}")


    print(sum_mul)




if __name__ == "__main__":
    main()