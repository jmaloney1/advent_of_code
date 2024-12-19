import os
def main():
    os.chdir(os.path.dirname(os.path.realpath(__file__)))

    with open("input/input") as f:
        count = 0
        for line in f:
            line = line.strip()
            if line == "":
                continue
            
            # Split on ':' to separate total from values
            total_str, values_str = line.split(':')
            total = int(total_str)
            
            # Split values string and convert to integers
            values = [int(x) for x in values_str.split()]
            
            print(f"Total: {total}, Values: {values}")

            def evaluate(values, total, wanted):
                if total > wanted:
                    return []

                if len(values) == 0:
                    return [total]
                
                value = values[0]

                mult = evaluate(values[1:], total * value, wanted)
                s = evaluate(values[1:], total + value, wanted)
                t = int(str(total) + str(value))
                cat = evaluate(values[1:], t, wanted)
                return mult + s + cat
            
            totals = evaluate(values, 0, total)
            matching_count = sum(1 for t in totals if t == total)
            if matching_count > 0:
                count += total
        print(count)

if __name__ == "__main__":
    main()