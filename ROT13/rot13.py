#!/usr/bin/env python3


#  rot13.py
#
#  Copyright 2017 Paolo "Plaoo" Monni
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
#
from string import ascii_uppercase
from string import ascii_lowercase
from string import ascii_letters

def how_use():
    print("example: rot13.py hello world \nResult: uryyb jbeyq")

def rot13(txt):
    dest = []
    ascii_loweruni = ascii_lowercase
    ascii_upperuni = ascii_uppercase
    ascii_letuni = ascii_letters

    for mov in txt:
        if mov not in ascii_letuni:
            dest.append(mov)
            continue
        if mov in ascii_letters:
            if mov in ascii_loweruni:
                alphab = ascii_loweruni

            elif mov in ascii_upperuni:
                alphab = ascii_upperuni

            x = alphab.index(mov)
            y = (x + 13) % 26
            dest.append(alphab[y])

    dest = ''.join(dest)
    return dest


def main(args):
    if (len(sys.argv) <= 1):
        how_use()
    elif (len(sys.argv) > 1):
        print("Result: " + rot13(' '.join(sys.argv[1:])))

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))