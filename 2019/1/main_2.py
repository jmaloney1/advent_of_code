import sys
import math

def main():
    total_fuel = 0
    for i in sys.stdin:
        try:
            mass = int(i)
        except ValueError:
            break

        fuel = calculate_fuel(mass)
        print(f"Fuel cost for {mass}: {fuel}")
        total_fuel = total_fuel + fuel

    print(f"Total fuel is: {total_fuel}")


def calculate_fuel(mass):
    fuel = math.floor(mass / 3) - 2
    if fuel > 0:
        return fuel + calculate_fuel(fuel)
    else:
        return 0


if __name__ == '__main__':
    main()

