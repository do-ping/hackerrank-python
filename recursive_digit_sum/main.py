#!/bin/python3


#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#


def superDigit(n, k):
    if not n:
        return 0
    if len(n) == 1 and k == 1:
        return int(n)

    s = sum((int(ch) for ch in n)) * k
    print(n, s)
    return superDigit(str(s), 1)


if __name__ == "__main__":
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    # first_multiple_input = input().rstrip().split()
    # n = first_multiple_input[0]
    # k = int(first_multiple_input[1])

    for nk in [("9875", 4, 8), ("29", 2, 4), ("11", 3, 6), ("2", 1, 2)]:
        n = nk[0]
        k = nk[1]
        expected = nk[2]
        result = superDigit(n, k)
        print("Result", n, k, result)
        assert result == expected

    # fptr.write(str(result) + '\n')
    # fptr.close()
