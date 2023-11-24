#!/bin/python3


#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    if k > 100 or k < 0 or k == 0:
        return s
    # 97 - 123 lower
    # 65 - 91 upper
    result = []
    for ch in s:
        if ch.isalpha():
            x = 65 if ch.isupper() else 97
            current_index = ord(ch) - x
            new_index = k % 26
            new_code = (current_index + new_index) % 26 + x
            ch = chr(new_code)

        result.append(ch)

    return "".join(result)


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    # n = int(input().strip())
    # s = input()
    # k = int(input().strip())

    for values in [
        ("There's-a-starman-waiting-in-the-sky", 3, "Wkhuh'v-d-vwdupdq-zdlwlqj-lq-wkh-vnb"),
        ("middle-Outz", 2, "okffng-Qwvb"),
        ("abc", 3, "def"),
        ("ABC", 26, "ABC")
    ]:
        s = values[0]
        k = values[1]
        result = caesarCipher(s, k)
        print(f"s={s} k={k} result={result}")
        assert values[2] == result

    # fptr.write(result + '\n')
    # fptr.close()
