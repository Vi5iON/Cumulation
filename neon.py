import common as c
from math import pow

def main():
    num = c.read('Enter a number.\n')
    if is_neon(num):
        print(f'{num} is a neon number.')
    else:
        print(f'{num} isn\'t a neon number.')


def is_neon(num: int)-> bool:
    if num == calculate(num):
        return True
    return False

def calculate(num: int)-> int:
    squared_num = pow(num, 2)
    res = 0
    
    while squared_num:
        res = c.add(res, c.digit_retriver(squared_num))
        squared_num = c.num_truncate(squared_num)

    return res

if __name__ == '__main__':
    main()