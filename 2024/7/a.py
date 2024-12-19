import os
def main():
    os.chdir(os.path.dirname(os.path.realpath(__file__)))

    with open("input/test") as f:
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

            def evaluate(values, total):
                if len(values) == 0:
                    return [total]
                
                value = values[0]

                return evaluate(values[1:], total + value) + evaluate(values[1:], total * value)
            
            totals = evaluate(values, 0)
            matching_count = sum(1 for t in totals if t == total)
            if matching_count > 0:
                print(f"Found {matching_count} ways to get {total}")

if __name__ == "__main__":
    main()