from common import read
from reverse import reverse

def main():
    lower = read('Enter lower range\n')
    upper = read('Enter upper range\n')
    print(f'Reversing in range({lower}, {upper})')
    for i in range(lower, upper):
        print(f'Reverse of {i} is {reverse(i)}')


if __name__ == '__main__':
    main()