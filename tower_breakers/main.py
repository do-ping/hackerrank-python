#!/bin/python3


#
# Complete the 'towerBreakers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#


def towerBreakers(n, m):
    if n == 0 or m == 0:
        return 1
    # no moves for 1st player from the start, 2d wins
    if m == 1:
        return 2
    # odd number of towers, both players will optimally reduce each tower to 1,
    # 1st player always makes the last move
    if n % 2 != 0:
        return 1
    # otherwise, 2d player destroys the last tower, optimally reducing it to 1
    return 2


if __name__ == "__main__":
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    # t = int(input().strip())

    # for t_itr in range(t):
    #     first_multiple_input = input().rstrip().split()
    #     n = int(first_multiple_input[0])
    #     m = int(first_multiple_input[1])

    for values in [
        (2, 6),  # 2 - 1 reduce 1st tower to 1, 2 reduce 2d tower to 1, no moves thus 2
        (2, 2),  # 2 - 1 reduce 1st tower to 1, 2 reduce 2d tower to 1, no moves thus 2
        (1, 4),  # 1 - 1 reduce tower to 1, 2 has no moves thus 1 is the winner
        (7, 12),  # 1 - 1st will always make last removal
        (4, 1),  # 2 - no moves for 1st player
    ]:
        n = values[0]
        m = values[1]
        result = towerBreakers(n, m)
        print(f"n={n} m={m} winner={result}")

        # fptr.write(str(result) + '\n')
    # fptr.close()
