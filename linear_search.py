import sys
from typing import List

sys.stdin = open("input.txt", "r")
sys.stdout = open("output.txt", "w")
sys.stderr = open("error.txt", "w")
# your remaining code


def search(arr: List[int], value: int) -> bool:
	"""
	Implement Linear Search on an array
	Time Complexity: O(n)

	:param arr: an array of integers
	:param value: an integer as the value to be searched
	:return bool: a boolean indicated if the value is in the array or not
	"""
	n: int = len(arr)

	for i in range(n):
		if arr[i] == value:
			return True

	return False
	

if __name__ == '__main__':
	value: int = 10
	arr: List[int] = list(map(int, input().strip().split(' ')))

	print(search(arr, value))