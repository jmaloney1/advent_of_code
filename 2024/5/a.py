import os
def main():
    os.chdir(os.path.dirname(os.path.realpath(__file__))) 
    with open("input/input") as f:
        lines = f.readlines()
    
    # Split into rules and sequences
    rules = []
    sequences = []
    parsing_rules = True
    
    for line in lines:
        line = line.strip()
        if not line:  # Empty line separates rules from sequences
            parsing_rules = False
            continue
            
        if parsing_rules:
            # Parse rules like "47|53" into tuples
            left, right = line.split('|')
            rules.append((int(left), int(right)))
        else:
            # Parse sequences like "75,47,61,53,29" into lists of integers
            sequences.append([int(x) for x in line.split(',')])
    
    print(f"Found {len(rules)} rules and {len(sequences)} sequences")
    print("Rules:", rules)
    print("Sequences:", sequences)

    def check_sequence(sequence):
        for i, s in enumerate(sequence):
            # enumerate before s
            for j, _s in enumerate(sequence[:i]):
                if (_s, s) not in rules:
                    print(f"Rule not found for {_s}|{s}")
                    return False

            # enumerate after s
            for j, _s in enumerate(sequence[i+1:]):
                if (s, _s) not in rules:
                    print(f"Rule not found for {s}|{_s}")
                    return False
        
        return True;

    valid_middle_sum = 0
    for sequence in sequences:
        if check_sequence(sequence):
            print(f"sequence {sequence} is valid")
            valid_middle_sum += sequence[len(sequence) // 2]

        else:
            print(f"sequence {sequence} is invalid")
    
    print(f"valid middle sum: {valid_middle_sum}")

if __name__ == "__main__":
    main()