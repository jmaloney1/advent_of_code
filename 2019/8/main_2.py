import sys


def main():
    image = list([int(c) for c in sys.stdin.readline().rstrip()])

    width = 25
    height = 6
    size = width * height

    layers = list(get_layers(image, size))
    
    layers.reverse()

    final_image = layers[0]

    for layer in layers:
        for i, pixel in enumerate(layer):
            if pixel != 2:
                final_image[i] = pixel

    print(f"Final image: {final_image}")
    for y in range(0, height):
        start = y * width
        end = start + width - 1
        [print((" ", 1)[p == 1], end="") for p in final_image[start:end]]
        print()


def get_layers(image, n):
    for i in range(0, len(image), n):
        yield image[i:i + n]


if __name__ == '__main__':
    main()

