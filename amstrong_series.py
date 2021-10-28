import common as c
from amstrong import is_amstrong

''' 
main block that uses is_amstrong() to find amstrong number
'''
def main() :
    num = c.read('Enter the number of amstrong numbers needed.\n')
    print(f'\nFinding {num} amstrong number(s):')
    count = 0
    i = 1
    while count < num :
        if is_amstrong(i) :
            print(i)
            count = c.add(count, 1)
        i = c.add(i, 1)
    print('Done.')


if __name__ == '__main__' :
    main()