from common import read
from reverse import reverse

def main():
    num = read('Enter a number.\n')
    if is_pallen(num):
        print(f'{num} is a pallendrome.')
    else:
        print(f'{num} isn\'t a pallendrome.')


def is_pallen(num: int)-> bool:
    if num == reverse(num):
        return True
    return False


if __name__ == '__main__':
    main()