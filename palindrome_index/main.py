#!/bin/python3


#
# Complete the 'palindromeIndex' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def palindromeIndex(s: str):
    start = -1
    end = len(s)
    to_remove = -1

    if end == 1:
        return to_remove
    if end == 2:
        return to_remove if s[0] == s[1] else 0
    if end == 3:
        if s[0] == s[2]:
            return -1
        elif s[0] == s[1]:
            return 2
        elif s[1] == s[2]:
            return 0
        else:
            return -1

    while start < end:
        start += 1
        end -= 1

        if start >= end:
            break

        if s[start] == s[end]:
            continue

        # not a palindrome, otherwise previous block would continue
        if to_remove >= 0:
            to_remove = -1
            break

        # try next from start
        # . . * . . . . . * . . - s[start] == s[end]         -> c=w -> False
        # 0 1 2 3 4 5 6 7 8 9 10
        # l f c w n n w c w f l
        # . . . * . . . . * . . - s[start + 1] == s[end]     -> w=w -> True
        # . . * . . . . * . . . - s[start]     == s[end - 1] -> c=c -> True
        # . . . . * . . * . . . - s[start + 2] == s[end - 1] -> n=c -> False ~ True = remove start 2 (c)
        # . . . * . . * . . . . - s[start + 1] == s[end - 2] -> w=w -> True  ~ True = remove end   8 (w)
        if s[start + 1] == s[end] and s[start] == s[end - 1]:
            if s[start + 2] == s[end - 1]:
                to_remove = start
                start += 1
                continue
            elif s[start + 1] == s[end - 2]:
                to_remove = end
                end -= 1
                continue

        if s[start + 1] == s[end]:
            to_remove = start
            start += 1
            continue
        elif s[start] == s[end - 1]:
            to_remove = end
            end -= 1
            continue
        else:
            break

    return to_remove


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    # q = int(input().strip())
    # for q_itr in range(q):
    #     s = input()
    for sr in [
        ("aaab", [3]),
        ("baa", [0]),
        ("aaa", [-1]),
        ("bcbc", [0, 3]),
        ("abcdba", [2, 4]),
        ("abcdefghijklmnnopqrstuvwxyzzyxwvutsrqponmlkjihgfedcba", [14]),
        ("lfcwnnwcwfl", [8]),
        ("lfwcwnnwcfl", [2])
    ]:
        s = sr[0]
        expected = sr[1]
        result = palindromeIndex(s)
        print(s, ":", expected, result, result in expected)
        assert result in expected
        # fptr.write(str(result) + '\n')
    # fptr.close()
