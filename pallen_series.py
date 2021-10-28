from common import read
from pallen import is_pallen


def main():
    lower = read('Enter lower range\n')
    upper = read('Enter upper range\n')
    print(f'Pallendromes in range({lower}, {upper})')
    for i in range(lower, upper):
        if is_pallen(i):
            print(f'{i}')


if __name__ == '__main__':
    main()