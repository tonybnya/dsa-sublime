"""
Must do Pattern Problems before starting DSA.
"""
import sys

sys.stdin = open("input.txt", "r")
sys.stdout = open("output.txt", "w")
sys.stderr = open("error.txt", "w")
# your remaining code


def pattern1(n: int) -> None:
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


def pattern2(n: int) -> None:
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
	

if __name__ == '__main__':
	n = int(input())
	pattern2(n)