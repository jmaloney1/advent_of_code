from collections import deque

if __name__ == '__main__':
    with open('input') as f:
        points_dict = {
            '(': 1,
            '[': 2,
            '{': 3,
            '<': 4,
        }
        all_points = []
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
                    q.clear()
                    break

            points = 0
            while len(q) > 0:
                c = q.pop()
                points *= 5
                points += points_dict[c]

            if points > 0:
                all_points.append(points)

        print(list(sorted(all_points))[len(all_points) // 2])

