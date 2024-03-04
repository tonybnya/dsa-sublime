"""
66. Plus One

You are given a large integer represented as an integer array digits,
where each digits[i] is the ith digit of the integer.
The digits are ordered from most significant to least significant
in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.
"""
import sys
from typing import List

sys.stdin = open("input.txt", "r")
sys.stdout = open("output.txt", "w")
sys.stderr = open("error.txt", "w")
# your remaining code


def solution(arr: List[int]) -> List[int]:
	"""
	Solution for Plus One

	:param arr: an array of integers
	:return List[int]: an array of integers 
	"""
	return [int(x) for x in str(int(''.join(map(str, arr))) + 1)]
	

if __name__ == '__main__':
	value = list(map(int, input().strip().split()))
	print(solution(value))
