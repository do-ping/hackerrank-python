#!/bin/python3


#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#


def minimumBribes(q):
    result = 0
    n = len(q)

    for i in range(n - 1, -1, -1):
        if q[i] - (i + 1) > 2:
            print("Too chaotic")
            return
        for j in range(max(0, q[i] - 2), i):
            if q[j] > q[i]:
                result += 1

    print(result)


if __name__ == "__main__":
    # t = int(input().strip())
    # for t_itr in range(t):
    #     n = int(input().strip())
    #     q = list(map(int, input().rstrip().split()))
    for q in [
        [1, 2, 3, 5, 4, 6, 7, 8],  # 1
        [4, 1, 2, 3],  # 3 > 2 = Too chaotic
        [2, 1, 5, 3, 4],  # 3
        [2, 5, 1, 3, 4],  # Too chaotic
        [5, 1, 2, 3, 7, 8, 6, 4],  # Too chaotic
        [1, 2, 5, 3, 7, 8, 6, 4],  # 7
    ]:
        print(q)
        minimumBribes(q)
