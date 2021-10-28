import common as c

def main():
    num = c.read('Enter a number.\n')
    print(f'Reverse of {num} is {reverse(num)}.')


def reverse(num: int)-> int:
    new_num = 0
    while num:
        new_num = c.add(new_num*10, c.digit_retriver(num))
        num = c.num_truncate(num)
    return new_num


if __name__ == '__main__':
    main()