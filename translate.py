#!/usr/bin/env python3
"""
Author : echeadle <echeadle@localhost>
Date   : 2023-09-16
Purpose: Take a string and translate it to a list of numbers
"""

import argparse
import re

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('positional',
                        metavar='str',
                        help='A positional argument')


    return parser.parse_args()


# --------------------------------------------------
def main():
    """Translate string to list of numbers"""
    new_list = []
    args = get_args()
    pos_arg = args.positional

    print(f'positional = "{pos_arg}"')
    #pos_arg = pos_arg.replace('-', '')
    nums = re.findall(r'\d+', pos_arg)
    print(f'nums: {nums}')
    for n in nums:
        new_list.append(int(n))

    print(new_list)
        

# --------------------------------------------------
if __name__ == '__main__':
    main()
