#!/bin/python3


#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#


def plusMinus(arr):
    if not arr:
        return

    n = len(arr)
    if n > 100:
        return

    positive = 0
    negative = 0
    zero = 0
    for e in arr:
        value = 1 + (e >> 31) - (-e >> 31)
        if value == 0:
            negative += 1
        elif value == 1:
            zero += 1
        else:
            positive += 1

    print("%.6f\n%.6f\n%.6f" % (positive / n, negative / n, zero / n))


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)

