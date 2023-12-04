#!/bin/python3


#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#


def diagonalDifference(arr):
    if not arr:
        return

    cell_i = 0
    diagonal_sum_l = 0
    diagonal_sum_r = 0

    for row in arr:
        diagonal_sum_l += row[cell_i]
        diagonal_sum_r += row[len(row) - 1 - cell_i]
        cell_i += 1

    return abs(diagonal_sum_l - diagonal_sum_r)


if __name__ == "__main__":
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    # n = int(input().strip())
    # arr = []
    # for _ in range(n):
    #     arr.append(list(map(int, input().rstrip().split())))

    for arr in (
        [[1, 2, 3], [4, 5, 6], [9, 8, 9]],  # 2
        [[11, 2, 4], [4, 5, 6], [10, 8, -12]],  # 15
        [[1, 2, 3, 4], [4, 3, 2, 1], [1, 2, 3, 4], [4, 3, 2, 1]],  # 4
    ):
        result = diagonalDifference(arr)
        print(arr)
        print(result)

    # fptr.write(str(result) + '\n')
    # fptr.close()
