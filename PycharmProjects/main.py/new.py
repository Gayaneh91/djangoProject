# import time
#
# start = time.perf_counter()
# def get_prime_number(n):
#     """
#      Description:
#       Given a prime number, the goal is get next prime number
#     Arguments:
#       Integer number
#     Libraries:
#       time
#     Dependencies & Supported Versions:
#       Python 3.10.x
#     """
#
#     for i in range(2, round(n ** 0.5)):
#         if n % i == 0:
#             return get_prime_number(n + 1)
#     return n
# n = int(input('Enter your number:'))
# print(get_prime_number(n))
# end = time.perf_counter()
# print(f'{end} - {start} = {end - start}')



#
# try:
#     n = int(input('Enter input:'))
#     for i in range(n):
#         if isinstance(n, int) and i < 6:
#             print('* ' * i)
#     while not n.isnumeric():
#         print('Try again.')
# except Exception as message:
#     print(f'Wrong input: {message}')

import sys
def row_rectangle(number, direction):
    if direction == 'left':
        for i in range(number):
            print((i + 1) * '*')
        else:
            for i in range(number):
                print((number-i) * ' ' + i * '*')
print(row_rectangle(4, 'right'))
list = [1, 2, 3, 4]
def check_input(n):
    """
    Check input if it not number try again.
    Args:
    Returns:
       number -
    """
#     while not n.isnumeric():
#         try:
#            n = int(input("Please enter the correct number type "))
#         except Exception as e:
#            print ("Try again")
#            n = input("Please enter the correct number type: ")
#     return n
    try:
        temp = int(n)
        return temp
    except ValueError:
        print("Only integer supported")
        sys.exit(1)

def check_direction(dr):
    """
    Function will check direction type.
    Direction type should be left or right.
    Args:
        dr - argument from command
    Returns:
        ---
    """
    if dr.lower() == 'right':
        return dr.lower()
    elif dr.lower() == 'left':
        return dr.lower()
    else:
        return 'left'


def main():
    try:
        number = sys.argv[1]
        direction = sys.argv[2]
    except IndexError:
        print("Please provide arguemnts. Number and direction")
        sys.exit(1)
    correct_number = check_input(number)
    correct_direction = check_direction(direction)
    row_rectangle(correct_number, correct_direction)


if __name__ == '__main__':
    main()












