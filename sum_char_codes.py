import sys
sys.stdin = open("input.txt", "r")
sys.stdout = open("output.txt", "w")
sys.stderr = open("error.txt", "w")
# your remaining code


def sum_char_codes0(string: str) -> int:
	"""
	Sum the code points of each character of a string
	Time Complexity: O(n)

	:param string: a string
	:return int: the sum of the code points
	"""
	s: int = 0
	n: int = len(string)

	for i in range(n):
		s += ord(string[i])

	return s


def sum_char_codes1(string: str) -> int:
	"""
	Sum the code points of each character of a string
	Time Complexity: O(n)

	:param string: a string
	:return int: the sum of the code points
	"""
	s: int = 0
	n: int = len(string)

	for i in range(n):
		s += ord(string[i])

	for i in range(n):
		s += ord(string[i])

	return s


def sum_char_codes2(string: str) -> int:
	"""
	Sum the code points of each character of a string
	Time Complexity: O(n)

	:param string: a string
	:return int: the sum of the code points
	"""
	s: int = 0
	n: int = len(string)

	for i in range(n):
		code = ord(string[i])
		# Capital E
		if code == 69:
			return s

		s += code

	return s


def sum_char_codes3(string: str) -> int:
	"""
	Sum the code points of each character of a string
	Time Complexity: O(n^2)

	:param string: a string
	:return int: the sum of the code points
	"""
	s: int = 0
	n: int = len(string)

	for i in range(n):
		for j in range(n):
			s += ord(string[i])

	return s


def sum_char_codes4(string: str) -> int:
	"""
	Sum the code points of each character of a string
	Time Complexity: O(n^3)

	:param string: a string
	:return int: the sum of the code points
	"""
	s: int = 0
	n: int = len(string)

	for i in range(n):
		for j in range(n):
			for k in range(n):
				s += ord(string[i])

	return s


if __name__ == '__main__':
	string: str = input()
	print(sum_char_codes4(string))