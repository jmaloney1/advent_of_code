if __name__ == '__main__':
    with open('input', 'r') as input:
        input_list = [line.strip() for line in input]

    bag_dict = {}
    for line in input_list:
        split = line.split(" contain ")
        outer_bag = split[0].replace(' bags', '')
        if outer_bag == 'shiny gold':
            continue
        inner_bags = ''.join(split[1:]).split(',')
        bag_dict[outer_bag] = []
        for bag_text in inner_bags:
            if bag_text == 'no other bags.':
                continue
            bag = bag_text.strip().replace(' bags', '').replace(' bag', '').replace('.', '')
            bag_dict[outer_bag].append(bag[2:])

        print(bag_dict)

    def search_bag(bag):
        if bag == 'shiny gold':
            return True

        for inner_bag in bag_dict[bag]:
            if search_bag(inner_bag):
                return True

        return False

    total = 0
    for bag in bag_dict:
        bag_search = search_bag(bag)
        print(f"{bag}: {bag_search}")
        if bag_search:
            total += 1

    print(total)

