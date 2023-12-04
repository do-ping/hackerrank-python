#!/bin/python3

from functools import reduce
from operator import add


#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#


def miniMaxSum(arr):
    if not arr or len(arr) > 5:
        return

    arr = sorted(arr)
    print(f"{reduce(add, arr[:-1])} {reduce(add, arr[1:])}")


if __name__ == "__main__":
    # arr = list(map(int, input().rstrip().split()))

    for arr in [
        [1, 3, 5, 7, 9],
        [1, 2, 3, 4, 5],
        [10000000, 20000000, 90000000, 50000000, 999999999],
    ]:
        miniMaxSum(arr)
