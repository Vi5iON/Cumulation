from common import read
from perfect_num import is_perfect

def main():
    lower = read('Enter the lower range.\n')
    upper = read('Enter the upper range.\n')
    print(f'\nPerfect numbers within the range ({lower},{upper}) are:')
    for i in range(lower, upper) :
        if is_perfect(i) :
            print(f'{i}')
    print('Done.')

if __name__ == '__main__' :
    main()