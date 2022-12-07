import util


class Node:
    def __init__(self, path, parent, children):
        self.path = path
        self.children = children
        self.parent = parent
        self.files = {}


if __name__ == '__main__':
    lines = util.read_input('input')
    root = Node('/', None, {})
    cur_dir = root
    cur_command = None
    for line in lines:
        command = line.strip().split(' ')
        if '$' == command[0]:
            cur_command = command[1]
            match cur_command:
                case 'cd':
                    if '/' == command[2]:
                        cur_dir = root
                    elif '..' == command[2]:
                        cur_dir = cur_dir.parent
                    else:
                        cur_dir = cur_dir.children[command[2]]
                case 'ls':
                    pass
        else:
            if 'dir' == command[0]:
                cur_dir.children[command[1]] = Node(cur_dir.path + f'{command[1]}/', cur_dir, {})
            else:
                cur_dir.files[command[1]] = int(command[0])

    def get_size(root, dir_sizes):
        s = sum(root.files.values()) + sum(map(lambda c: get_size(c, dir_sizes), root.children.values()))
        dir_sizes += [s]
        return s


    dir_sizes = []
    total_size = get_size(root, dir_sizes)
    dir_sizes = sorted(dir_sizes)
    unused = 70000000 - total_size
    required = 30000000 - unused
    print(f'Total: {total_size}')
    print(f'Required: {required}')
    print(dir_sizes)
    print(next(filter(lambda d: d >= required, dir_sizes)))
