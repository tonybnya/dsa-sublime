"""
118. Pascal's Triangle

Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly
above it as shown:

1
11
121
1331
14641
"""
from typing import List
import sys

sys.stdin = open("input.txt", "r")
sys.stdout = open("output.txt", "w")
sys.stderr = open("error.txt", "w")
# your remaining code


def solution(rows: int) -> List[List[int]]:
	"""
	Solution for Pascal Triangle

	:param rows: an integer as the number of rows of the triangle
	:return List[List[int]]: a matrix representing the Pascal Triangle 
	"""
	triangle: List[List[int]] = [[1]]

	for i in range(1, rows + 1):
		row = [1]
		for j in range(1, i):
			row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])

		row.append(1)
		triangle.append(row)

	return triangle[rows]	


if __name__ == '__main__':
	rows: int = int(input())
	print(solution(rows))
