from common import read
from prime import is_prime

'''
main block that accepts upper and lower limit.
Finds the prime numbers within this range.
'''
def main() :
    lower = read('Enter the lower range.\n')
    upper = read('Enter the upper range.\n')
    print(f'\nPrime numbers within the range ({lower},{upper}) are:')
    for i in range(lower, upper) :
        if is_prime(i) :
            print(f'{i}')
    print('Done.')

        
if __name__ == '__main__' :
    main()