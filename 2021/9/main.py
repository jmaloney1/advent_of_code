if __name__ == '__main__':
    with open('input') as f:
        height_map = ['9' + l.strip() + '9' for l in f]

        # wrap in 9s
        height_map.insert(0, '9' * len(height_map[0]))
        height_map.append('9' * len(height_map[0]))

        t = 0
        for y in range(1, len(height_map)-1):
            line = height_map[y]
            for i in range(1, len(line)-1):
                w_y = [h[i] for h in height_map[y-1:y+2]]
                w_x = line[i-1:i+2]
                if w_x[0] > w_x[1] < w_x[2] and w_y[0] > w_y[1] < w_y[2]:
                    print((w_x[1], (i, y)))
                    t += int(w_x[1]) + 1

        print(t)