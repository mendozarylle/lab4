#!/usr/bin/env python3
# Author ID: rmendoza10@myseneca.ca

def is_digits(sobj):
    # Loop through each character in sobj
    for char in sobj:
        # If a character is not a digit, return False
        if not char.isdigit():
            return False
    # If all characters are digits, return True
    return True

if __name__ == '__main__':
    test_list = ['x3058', '3058', '8503x', '8503']
    for item in test_list:
        if is_digits(item):
            print(item, 'is an integer.')
        else:
            print(item, 'is not an integer.')