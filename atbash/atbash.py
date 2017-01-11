#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  atbash.py
#  
#  Copyright 2016 Paolo "Plaoo" Monni 
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
import sys
from string import ascii_uppercase
from string import ascii_lowercase
from string import ascii_letters 
  
def how_use():
	
	
	print("example: atbash.py hello world \nResult: svool dliow")

def atbash(txt):
	dest = []
	ascii_loweruni = ascii_lowercase
	ascii_upperuni = ascii_uppercase
	ascii_letuni = ascii_letters
	#reverse alphabet
	ascii_lowerunirev = ascii_lowercase[::-1]
	ascii_upperunirev = ascii_uppercase[::-1]
	ascii_letunirev = ascii_letters[::-1]
	
	
	for mov in txt:
		#not a ascii character
		if mov not in ascii_letuni:
			dest.append(mov)
			continue
		if mov in ascii_letters:
			if mov in ascii_loweruni:
				#lower case
				alphab = ascii_lowerunirev
				x = alphab.index(mov)
				dest.append(ascii_loweruni[x])
				
			elif mov in ascii_upperuni:
				#upper case
				alphab = ascii_upperunirev
				#x position in reverse alphabet
				x = alphab.index(mov)
				#position x in normal alphabet
				dest.append(ascii_upperuni[x])

	dest = ''.join(dest)
	return dest
	
def main(args):
	if(len(sys.argv)<=1):
		how_use()
	elif(len(sys.argv)>1):
		print("Result: " + atbash(' '.join(sys.argv[1:])))
		


if __name__ == '__main__':
	import sys
	sys.exit(main(sys.argv))
