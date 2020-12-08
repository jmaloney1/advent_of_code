if __name__ == '__main__':
    with open('input', 'r') as input:
        input_list = [line.strip() for line in input]

    bag_dict = {}
    for line in input_list:
        split = line.split(" contain ")
        outer_bag = split[0].replace(' bags', '')
        inner_bags = ''.join(split[1:]).split(',')
        bag_dict[outer_bag] = []
        for bag_text in inner_bags:
            if bag_text == 'no other bags.':
                continue
            bag = bag_text.strip().replace(' bags', '').replace(' bag', '').replace('.', '')
            count = int(bag[0:2])
            colour = bag[2:]
            bag_dict[outer_bag].append((count, colour))

        print(bag_dict)

    def search_bag(bag):
        total = 1
        for inner_bag_tuple in bag_dict[bag]:
            total += search_bag(inner_bag_tuple[1]) * inner_bag_tuple[0]

        return total

    bag_search = search_bag('shiny gold') - 1
    print(bag_search)

