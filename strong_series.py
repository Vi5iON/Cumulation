from strong import is_strong
import common as c
''' 
main block that uses find_strong to check find strong number(s)
'''

def main() :
    num = c.read('Enter the number of strong numbers needed.\n')
    print(f'\nFinding {num} strong number(s):')
    if num < 4 :
        find_strong(num)
    else :
        find_strong(4)
    print('Found availabe strong numbers.')

# to print specified number of strong numbers
def find_strong(num: int):
    count = 0
    i = 1
    while count < num :
        if is_strong(i) :
            print(i)
            count= c.add(count, 1)
        i= c.add(i, 1) 


if __name__ == '__main__' :
    main()