#!/bin/python3


#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#


def lonelyinteger(a):
    if not a:
        return
    if len(a) == 1:
        return a[0]

    a = sorted(a)
    unique = None
    skip = False
    for i in range(len(a)):
        if skip:
            skip = False
            continue

        if i == len(a) - 1 and not unique:
            unique = a[-1]
            break

        current = a[i]
        next = a[i + 1]
        if current != next:
            unique = current
            break

        skip = True

    return unique


if __name__ == "__main__":
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    # n = int(input().strip())
    # a = list(map(int, input().rstrip().split()))

    for a in [
        [1, 2, 3, 4, 3, 2, 1],  # 4
        [2, 2, 11, 11, 12, 13, 22, 13, 12, 22, 9],  # 9
        [9, 8, 7, 7, 8, 9, 1],  # 1
    ]:
        result = lonelyinteger(a)
        print(a)
        print(result)

    # fptr.write(str(result) + '\n')
    # fptr.close()
