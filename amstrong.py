from math import pow
import common as c

''' 
main block that uses is_amstrong() to check if its amstrong number
'''
def main() :
    num = c.read('Enter the number.\n')
    if is_amstrong(num) :
        print(f'{num} is amstrong number.')
    else :
        print(f'{num} isn\'t amstrong number.')


# is_amstrong() returns if true or false based on calculate result from calculate()
def is_amstrong(num: int)->bool :
    if num == calculate(num) :
        return True
    else :
        return False


# does necessary calculation for finding if it is a amstrong number
def calculate(num: int)->int :
    res = 0
    power = num_of_digits(num)
    while num :
        digit = c.digit_retriver(num)
        res = c.add(res, pow(digit, power))
        num = c.num_truncate(num)
    return res


# finds number of digits in the number
def num_of_digits(num: int)->int :
    count = 0
    while num :
        num = c.num_truncate(num)
        count = c.add(count,1)
    return count


if __name__ == '__main__' :
    main()