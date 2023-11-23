# You can modify at most three lines in the given code. You cannot add or remove lines of code.
def findZigZagSequence(a, n):
    a.sort()
    mid = int((n - 1)/2)  # 1
    a[mid], a[n - 1] = a[n - 1], a[mid]

    st = mid + 1
    ed = n - 2  # 2
    while (st <= ed):
        a[st], a[ed] = a[ed], a[st]
        st = st + 1
        ed = ed - 1  # 3

    for i in range(n):
        if i == n - 1:
            print(a[i])
        else:
            print(a[i], end=' ')
    return


# test_cases = int(input())
# for cs in range(test_cases):
#     n = int(input())
#     a = list(map(int, input().split()))
#     findZigZagSequence(a, n)

if __name__ == '__main__':
    for arr in [
        [2, 3, 5, 1, 4],  # 1 2 5 4 3
    ]:
        findZigZagSequence(arr, len(arr))
