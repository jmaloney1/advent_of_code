if __name__ == '__main__':

    with open('test_input') as f:

        segments = []
        max_x = 0
        max_y = 0

        input_values = []
        for line in f:
            s = line.strip().split(' | ')
            signal_pattern = s[0].split(' ')
            output_values = s[1].split(' ')

            input_values.append((signal_pattern, output_values))

        # signal -> possible segment
        segment_dict = {
            'a': set('abcdefg'),
            'b': set('abcdefg'),
            'c': set('abcdefg'),
            'd': set('abcdefg'),
            'e': set('abcdefg'),
            'f': set('abcdefg'),
            'g': set('abcdefg'),
        }
        for i in list(input_values):
            if all(filter(lambda w: len(w) == 1, segment_dict)):
                print(segment_dict)
            signal_pattern = i[0]
            output_values = i[1]

            for o in output_values:
                set_o = set(o)
                if len(o) == 2:
                    for s in 'abdeg':
                        if segment_dict[s] != set_o:
                            segment_dict[s] = segment_dict[s] - set_o
                    for s in 'cf':
                        segment_dict[s] = segment_dict[s].union(set_o)

                elif len(o) == 4:
                    for s in 'aeg':
                        if len(segment_dict[s]) != 1 and segment_dict[s] != set_o:
                            segment_dict[s] = segment_dict[s] - set_o
                    for s in 'acdf':
                        segment_dict[s] = segment_dict[s].union(set_o)
                elif len(o) == 3:
                    for s in 'acf':
                        if len(segment_dict[s]) != 1 and segment_dict[s] != set_o:
                            segment_dict[s] = segment_dict[s] - set_o
                    for s in 'bdeg':
                        segment_dict[s] = segment_dict[s].union(set_o)

                for s in 'abcdefg':
                    if len(segment_dict[s]) == 1:
                        for x in set('abcdefg') - set(s):
                            segment_dict[x] = segment_dict[x] - set(s)
                # elif len(o) == 7:
                #     for s in 'acf':
                #         if len(segment_dict[s]) != 1 and segment_dict[s] == set_o:
                #             segment_dict[s] = segment_dict[s] - set_o
                #     for s in 'bdeg':
                #         segment_dict[s] = segment_dict[s].union(set_o)
            print(segment_dict)

        print(segment_dict)
