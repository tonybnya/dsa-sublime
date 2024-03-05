"""
Must do Pattern Problems before starting DSA.
22 patterns, named like this pattern00...pattern21

Patterns == Nested Loops

For most of the patterns, we have to handle two nested loops:
an outer loop for rows (lines) & an inner loop for columns.

Below are the 4 steps to follow in order to print any pattern.

Step 1: For the outer loop, count the number of lines (rows)
Step 2: For the inner loop, focus on the columns and connect them somehow with the rows.
Step 3: Whatever you have to print, like '*', print them inside the inner loop
Step 4: Observe symmetry

The first 3 steps are mandatory.
The last is optional and can be applicable for some patterns.
"""
import sys

sys.stdin = open("input.txt", "r")
sys.stdout = open("output.txt", "w")
sys.stderr = open("error.txt", "w")
# your remaining code


def pattern00(n: int) -> None:
	"""
	*****
	*****
	*****
	*****
	*****

	:param n: integer as input (number of rows)
	"""
	for i in range(n):
		for j in range(n):
			print('*', end='')
		print()


def pattern01(n: int) -> None:
	"""
	*
	**
	***
	****
	*****

	:param n: integer as input (number of rows)
	"""
	for i in range(n):
		for j in range(i + 1):
			print('*', end='')
		print()


def pattern02(n: int) -> None:
	"""
	1
  	12
  	123
  	1234
  	12345

	:param n: integer as input (number of rows)
 	"""
	for i in range(n):
		for j in range(i + 1):
			print(j + 1, end='')
		print()


def pattern03(n: int) -> None:
	"""
	1
  	22
  	333
  	4444
  	55555

	:param n: integer as input (number of rows)
 	"""
	for i in range(n):
		for j in range(i + 1):
			print(i + 1, end='')
		print()


def pattern04(n: int) -> None:
	"""
	*****
	****
	***
	**
	*

	:param n: integer as input (number of rows)
 	"""
	for i in range(n):
		for j in range(n - i):
			print('*', end='')
		print()


def pattern05(n: int) -> None:
	"""
  	12345
  	1234
  	123
  	12
	1

	:param n: integer as input (number of rows)
 	"""
	for i in range(n):
		for j in range(n - i):
			print(j + 1, end='')
		print()


def pattern06(n: int) -> None:
	"""
	    *
	   ***
	  *****
	 *******
	*********

	:param n: integer as input (number of rows)
 	"""
	for i in range(n):
		# spaces
		for j in range(n - i - 1):
			print(' ', end='')
		# stars
		for j in range(2 * i + 1):
			print('*', end='')
		# spaces
		for j in range(n - i - 1):
			print(' ', end='')

		print()


def pattern07(n: int) -> None:
	"""
	*********
	 *******
	  *****
	   ***
	    *

	:param n: integer as input (number of rows)
 	"""
	for i in range(n):
		# spaces
		for j in range(i):
			print(' ', end='')
		# stars
		for j in range(2 * (n - i) - 1):
			print('*', end='')
		# spaces
		for j in range(i):
			print(' ', end='')

		print()
	

if __name__ == '__main__':
	# n = list(map(int, input().strip().split(' ')))
	# print(n)
	# pattern01(n)
	with open('input.txt') as file:
		for item in file.readlines():
			n = int(item.strip())
			pattern07(n)
			print()