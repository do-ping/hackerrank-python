#!/bin/python3


#
# Complete the 'findMedian' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#


def findMedian(arr):
    return sorted(arr)[int(len(arr) / 2)]


if __name__ == "__main__":
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # n = int(input().strip())

    # arr = list(map(int, input().rstrip().split()))

    for arr in [
        [0, 1, 2, 4, 6, 5, 3],  # 3
        [99, 119, 666, 231, 453, 777, 878],  # 453
        [11, 10, 9, 8, 7, 6, 5, 4, 3],  # 7
    ]:
        result = findMedian(arr)
        print(arr)
        print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
