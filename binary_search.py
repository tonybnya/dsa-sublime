import sys
from typing import List

sys.stdin = open("input.txt", "r")
sys.stdout = open("output.txt", "w")
sys.stderr = open("error.txt", "w")
# your remaining code


def search(arr: List[int], value: int) -> bool:
	"""
	Implement Binary Search on an array
	Time Complexity: O(logn)

	:param arr: an array of integers
	:param value: an integer as the value to be searched
	:return bool: a boolean indicated if the value is in the array or not
	"""
	n: int = len(arr)
	lo: int = 0
	hi: int = n - 1

	while (lo <= hi):
		mid: int = (lo + hi) // 2
		if arr[mid] == value:
			return True
		elif arr[mid] > value:
			hi = mid - 1
		else:
			lo = mid + 1

	return False
	

if __name__ == '__main__':
	arr: List[int] = list(map(int, input().strip().split(' ')))

	for i in range(-1, 12):
		value: int = i
		print(search(arr, value))