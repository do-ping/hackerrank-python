#!/bin/python3


#
# Complete the 'gridChallenge' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY grid as parameter.
#

def gridChallenge(grid):
    if not grid:
        return "NO"

    if len(grid) == 1:
        return "YES"

    row_length = len(grid[0])
    previous_row = None
    for row in (sorted(row) for row in grid):
        if previous_row:
            for col_n in range(row_length):
                if row[col_n] < previous_row[col_n]:
                    return "NO"

        previous_row = row

    return "YES"


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    # t = int(input().strip())
    # for t_itr in range(t):
    #     n = int(input().strip())
    #     grid = []
    #     for _ in range(n):
    #         grid_item = input()
    #         grid.append(grid_item)
    for grid_ in [
        (["abc", "ade", "efg"], "YES"),
        (["ebacd", "fghij", "olmkn", "trpqs", "xywuv"], "YES"),
        (["abcdef", "aacdef", "bczxb"], "NO")
    ]:
        grid = grid_[0]
        expected = grid_[1]
        result = gridChallenge(grid)
        print(grid, expected, result)
        assert expected == result
        # fptr.write(result + '\n')
    # fptr.close()
