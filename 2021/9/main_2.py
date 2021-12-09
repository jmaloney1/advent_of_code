def update_segment_dict(i, used_segs, segment_dict):
    used_segs = set(used_segs)
    i = set(i)
    for s in set('abcdefg') - i:
        segment_dict[s] = segment_dict[s] - used_segs
    for s in i:
        segment_dict[s] = segment_dict[s].intersection(used_segs)

    for key in segment_dict:
        if len(segment_dict[key]) == 1:
            for other_key in segment_dict:
                if key != other_key:
                    segment_dict[other_key] = segment_dict[other_key] - set(segment_dict[key])


if __name__ == '__main__':
    total = 0
    with open('input') as f:

        values = {
            'abcefg': 0,
            'cf': 1,
            'acdeg': 2,
            'acdfg': 3,
            'bcdf': 4,
            'abdfg': 5,
            'abdefg': 6,
            'acf': 7,
            'abcdefg': 8,
            'abcdfg': 9,
        }
        for line in f:
            s = line.strip().split(' | ')
            signal_pattern = s[0].split(' ')
            output = s[1].split(' ')

            # variables named after segment count
            two = list(map(set, filter(lambda p: len(p) == 2, signal_pattern)))[0]
            three = list(map(set, filter(lambda p: len(p) == 3, signal_pattern)))[0]
            four = list(map(set, filter(lambda p: len(p) == 4, signal_pattern)))[0]
            fives = list(map(set, filter(lambda p: len(p) == 5, signal_pattern)))
            sixes = list(map(set, filter(lambda p: len(p) == 6, signal_pattern)))
            seven = list(map(set, filter(lambda p: len(p) == 7, signal_pattern)))[0]

            segment_dict = dict()
            segment_dict['a'] = three - two
            segment_dict['b'] = four - two
            segment_dict['c'] = two
            segment_dict['f'] = two
            segment_dict['d'] = four - two

            for s in sixes:
                if len(s.difference(four.union(segment_dict['a']))) == 1:
                    segment_dict['g'] = s.difference(four.union(segment_dict['a']))
                    segment_dict['e'] = seven - s
                    break

            for s in sixes:
                if s.union(two) == s and segment_dict['e'].union(s) == s:
                    segment_dict['d'] = seven - s

            segment_dict['b'] = segment_dict['b'] - segment_dict['d']

            for s in sixes:
                if s.union(two) != s:
                    segment_dict['c'] = two - s
                    segment_dict['f'] = two - segment_dict['c']

            for key in segment_dict:
                segment_dict[key] = segment_dict[key].pop()

            flipped = dict()
            for key in segment_dict:
                flipped[segment_dict[key]] = key

            t = 0
            d = 1
            for o in reversed(output):
                o_v = ''.join(sorted([flipped[c] for c in o]))
                t += values[o_v] * d
                d *= 10
            print(t)
            total += t

        print(total)

