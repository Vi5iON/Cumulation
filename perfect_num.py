from common import read, add

def main():
    num = read('Enter the number.\n')
    if is_perfect(num):
        print(num,'is a perfect number.')
    else :
        print(num,'isn\'t a perfect number.')

def is_perfect(num: int)-> int:
    if sum_of_factors(num) == num :
        return True
    return False

def sum_of_factors(num: int)-> int:
    i = 1
    res = 0
    while i < num :
        if num % i == 0 :
            res = add(res, i)
        i = add(i, 1)
    return res


if __name__ == '__main__' :
    main()