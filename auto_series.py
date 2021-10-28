from common import read
from auto_num import is_automorphic


def main():
    lower = read('Enter lower range\n')
    upper = read('Enter upper range\n')
    print(f'Automorphic numbers in range({lower}, {upper})')
    for i in range(lower, upper):
        if is_automorphic(i):
            print(f'{i}')
    print('Done.')


if __name__ == '__main__':
    main()