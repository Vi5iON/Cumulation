from common import read
from neon import is_neon

def main() :
    lower = read('Enter the lower range.\n')
    upper = read('Enter the upper range.\n')
    print(f'\nNeon numbers within the range ({lower},{upper}) are:')
    for i in range(lower, upper) :
        if is_neon(i) :
            print(f'{i}')
    print('Done.')

if __name__ == '__main__':
    main()