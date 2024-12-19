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
                    return False

            # enumerate after s
            for j, _s in enumerate(sequence[i+1:]):
                if (s, _s) not in rules:
                    return False
        
        return True;
    
    def create_valid_sequences(invalid_sequence):
        sequence = [invalid_sequence[0]]
        for _s in invalid_sequence[1:]:
            for j in range(len(sequence) + 1):
                if check_sequence(sequence[:j] + [_s] + sequence[j:]):
                    sequence = sequence[:j] + [_s] + sequence[j:]
                    break

        return sequence

    middle_value_sum = 0
    for sequence in sequences:
        if not check_sequence(sequence):
            valid_sequence = create_valid_sequences(sequence)
            print(f"valid_sequence: {valid_sequence}")
            middle_value_sum += (valid_sequence[len(valid_sequence) // 2])

    print(f"middle_value_sum: {middle_value_sum}")

if __name__ == "__main__":
    main()
