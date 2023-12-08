def read_input(file: str, strip: bool = False):
    with open(file) as f:
        if strip:
            return map(lambda x: x.strip(), f.readlines())
        else:
            return f.readlines()
