"""Generate random names for Dungeons and Dragons"""
import sys
import random


def main():
    """Main function"""
    print("Welcome to your random name generator!\n")
    print("Here's what your DnD name would be:\n\n")

    first = ('Fahnud', 'Aden', 'Bruu',
             'Brobrom', 'Morgim', 'Pal',
             'Zarcom', 'Blum', 'Diohvechof',
             'Nurif', 'Relvonredj', 'Brejas',
             'Chih', 'Jey', 'Irnuescur', 'Fieluel')

    last = ('Custid', 'Neshe', 'Freereaper',
            'Spiritwound', 'Keg', 'Shurdersk',
            'Farrowslayer', 'Axegust', 'Lathenthihr',
            'Ninthuem', 'Habivrorke', 'Gomzidzi',
            'Xue', 'Zieng', 'Pizoha', 'Siscuston')

    while True:
        first_name = random.choice(first)
        last_name = random.choice(last)

        print("\n\n")
        print("{} {}".format(first_name, last_name), file=sys.stderr)
        print("\n\n")

        try_again = input('Do you want to continue? (Enter "n" if no)\n')

        if try_again.lower() == 'n':
            break


if __name__ == "__main__":
    main()
