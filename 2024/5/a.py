def main():
    with open("5/input/test") as f:
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

if __name__ == "__main__":
    main()