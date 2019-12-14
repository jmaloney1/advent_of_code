import sys


def main():
    image = list([int(c) for c in sys.stdin.readline().rstrip()])

    layers = list(get_layers(image, 25 * 6))

    layer = min(layers, key=lambda l: l.count(0))

    print(f"Number of 1s * 2s: {layer.count(1) * layer.count(2)}")


def get_layers(image, n):
    for i in range(0, len(image), n):
        yield image[i:i + n]


if __name__ == '__main__':
    main()

