#!/usr/bin/env python3
"""
Author : echeadle <echeadle@localhost>
Author : Copilot
Date   : 2023-11-24
Purpose: Take a string and translate it to a list of numbers
"""

import argparse
import re

def get_args():
    """Parse command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Take a string and translate it to a list of numbers',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('string',
                        metavar='str',
                        help='Input string')

    return parser.parse_args()


def extract_numbers(string_arg):
    nums = re.findall(r'\d+', string_arg)
    new_list = []
    for n in nums:
        new_list.append(int(n))
    return new_list


def main():
    args = get_args()
    string = args.string
    numbers = extract_numbers(string)
    print(numbers)


if __name__ == '__main__':
    main()
