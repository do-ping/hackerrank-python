#!/bin/python3


#
# Complete the 'flippingMatrix' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY matrix as parameter.
#


def flippingMatrix(matrix):
    matrix_size = len(matrix)
    submatrix_size = matrix_size // 2 + matrix_size % 2
    max_sum = 0  # sum of max *
    # row_n = 0, col_n = 0
    # r|c 0 1 2 3
    # 0  [* . . *]
    # 1  [. . . .]
    # 2  [. . . .]
    # 3  [* . . *] => max *
    # row_n = 0, col_n = 1
    # r|c 0 1 2 3
    # 0  [. * * .]
    # 1  [. . . .]
    # 2  [. . . .]
    # 3  [. * * .] => max *
    # row_n = 1, col_n = 0
    # r|c 0 1 2 3
    # 0  [. . . .]
    # 1  [* . . *]
    # 2  [* . . *]
    # 3  [. . . .] => max *
    # row_n = 1, col_n = 1
    # r|c 0 1 2 3
    # 0  [. . . .]
    # 1  [. * * .]
    # 2  [. * * .]
    # 3  [. . . .] => max *
    for row_n in range(submatrix_size):
        for col_n in range(submatrix_size):
            top_left = matrix[row_n][col_n]
            top_right = matrix[row_n][matrix_size - 1 - col_n]
            bottom_left = matrix[matrix_size - 1 - row_n][col_n]
            bottom_right = matrix[matrix_size - 1 - row_n][matrix_size - 1 - col_n]

            max_sum += max(top_left, top_right, bottom_left, bottom_right)

    return max_sum


if __name__ == "__main__":
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    # q = int(input().strip())

    # for q_itr in range(q):
    #     n = int(input().strip())
    #
    #     matrix = []
    #
    #     for _ in range(2 * n):
    #         matrix.append(list(map(int, input().rstrip().split())))

    for matrix in [
        [[1, 2], [3, 4]],  # 4 - reverse row 1, reverse column 1
        [
            [112, 42, 83, 119],
            [56, 125, 56, 49],
            [15, 78, 101, 43],
            [62, 98, 114, 108],
        ],  # 414
        [[1, 2, 3], [4, 5, 6], [7, 8, 9]],  # 28
    ]:
        result = flippingMatrix(matrix)
        for row in matrix:
            print(row)
        print(f"{result}")

        # fptr.write(str(result) + '\n')

    # fptr.close()
