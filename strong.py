from math import factorial as fact
import common as c

''' 
main block that uses is_strong() to check if its strong number
'''
def main() :
    num = c.read('Enter the number.\n')
    if is_strong(num) :
        print(f'{num} is a strong number.')
    else :
        print(f'{num} isn\'t a strong number.')


# is_strong() returns if true or false based on caluclate result from calculate()
def is_strong(num:int)-> bool:
    if calculate(num) == num:
        return True
    return False


# does necessary calculation for finding if it is a strong number
def calculate(num:int)-> int:
    res = 0
    while num :
        res = c.add(res, fact(c.digit_retriver(num)))
        num = c.num_truncate(num)
    return res


if __name__ == '__main__' :
    main()