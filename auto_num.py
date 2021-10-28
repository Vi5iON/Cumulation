import common as c
from math import pow

def main() :
    num = c.read('Enter a number.\n')
    if is_automorphic(num) :
        print(f'{num} is automorphic.')
    else:
        print(f'{num} isn\'t automorphic.')


#checks if the given number is automorphic
def is_automorphic(num: int)->bool :
    squared = int(pow(num, 2))
    while num :
        if c.digit_retriver(num) != c.digit_retriver(squared):
            return False
        num = c.num_truncate(num)
        squared = c.num_truncate(squared)
    return True


if __name__ == '__main__':
    main()