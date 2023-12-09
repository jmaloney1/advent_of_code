def read_input(file: str, strip: bool = False, index: bool = False):
    with open(file) as f:
        r = f.readlines()
        if strip:
            r = map(lambda x: x.strip(), r)

        if index:
            r = enumerate(r)

        return r
