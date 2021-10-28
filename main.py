from common import read
import index
import os

def main():
    print('++++++++++++++ Choose from the below +++++++++++++')
    choice = read('1. Single output\n2. Series output.\n')
    if choice == 1:
        single_output()
    elif choice == 2:
        series_output()
    else:
        print('\nInvalid choice.')

def single_output():
    print('\nYou selected "Single output".\n+++++++++++ Pick one ++++++++++')
    choice= display_menu()
    index.single(choice)


def series_output():
    print('You selected "Series output".\n+++++++++++ Pick one ++++++++++')
    choice= display_menu()
    index.series(choice)
    

def display_menu()-> int:
    print('1. Prime number\n2. Perfect number\n3. Neon number\n4. Automorphic number')
    return read('5. Reverse a number\n6. Pallendrome number\n7. Strong number\n8. Amstrong number\n')

if __name__ == '__main__':
    main()
    while input('\nDo you wish to continue? (y/n)\n') == 'y':
        os.system('cls')
        main()
    print('++++++++Thank you+++++++++')