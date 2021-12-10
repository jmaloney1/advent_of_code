from collections import deque

if __name__ == '__main__':
    with open('input') as f:
        points_dict = {
            ')': 3,
            ']': 57,
            '}': 1197,
            '>': 25137
        }
        points = 0
        for line in f:
            q = deque()
            for c in line.strip():
                if c in {'(', '[', '{', '<'}:
                    q.append(c)
                else:
                    opening_c = q.pop()
                    if c == ')' and opening_c == '(':
                        continue
                    elif c == ']' and opening_c == '[':
                        continue
                    elif c == '}' and opening_c == '{':
                        continue
                    elif c == '>' and opening_c == '<':
                        continue

                    print(f"Broke on {c}")
                    points += points_dict[c]
                    break

        print(points)

