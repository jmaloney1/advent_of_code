import os

def main():
    os.chdir(os.path.dirname(os.path.realpath(__file__)))
    
    with open("input/input") as f:
        line = f.readline().strip()
        # Convert string of digits to list of integers
        digits = [int(x) for x in line]
        print(f"Digits: {digits}")
        
    disk_map = ''
    i = 0
    blank = False 
    for d in digits:
        if not blank:
            disk_map += str(i) * d
            i += 1
            blank = True
        else:
            disk_map += ('.' * d)
            blank = False

    print(disk_map)

    new_disk_map = list(disk_map)
    i = 0
    j = len(disk_map) - 1
    while '.' in new_disk_map:
        while new_disk_map[i] != '.':
            i += 1
        while disk_map[j] == '.':
            j -= 1
            new_disk_map.pop()
        new_disk_map[i] = new_disk_map[j]
        i += 1
        j -= 1
        new_disk_map.pop()

    print(''.join(new_disk_map))

    i = 0
    s = 0
    for c in new_disk_map:
        if not (c == '.'):
            s += int(c) * i
        i += 1
    print(s)

if __name__ == "__main__":
    main()
