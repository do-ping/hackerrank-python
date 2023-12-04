#!/bin/python3


#
# Complete the 'missingWords' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING s
#  2. STRING t
#


def missingWords(s, t):
    if not s or not t or s == t:
        return []

    s_words, t_words = s.split(" "), t.split(" ")
    i, j = 0, 0
    result = []

    while i < len(s_words) and j < len(t_words):
        if s_words[i] == t_words[j]:
            i += 1
            j += 1
        else:
            result.append(s_words[i])
            i += 1

    result.extend(s_words[i:])
    return result


if __name__ == "__main__":
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    # s = input()
    # t = input()

    for data in [
        ["", "", []],
        ["one", "", []],
        ["", "two", []],
        ["three", "three", []],
        [
            "I mostly use Python for coding challenges because it's easier",
            "mostly Python it's easier",
            ["I", "use", "for", "coding", "challenges", "because"],
        ],
        ["I like cheese", "like", ["I", "cheese"]],
        [
            "I am using HackerRank to improve programming",
            "am HackerRank to improve",
            ["I", "using", "programming"],
        ],
        [
            "Python is an easy to learn powerful programming language It has efficient high-level data structures and a "
            "simple but effective approach to objectoriented programming Python elegant syntax and dynamic typing",
            "Python is an easy to learn powerful programming language",
            [
                "It",
                "has",
                "efficient",
                "high-level",
                "data",
                "structures",
                "and",
                "a",
                "simple",
                "but",
                "effective",
                "approach",
                "to",
                "objectoriented",
                "programming",
                "Python",
                "elegant",
                "syntax",
                "and",
                "dynamic",
                "typing",
            ],
        ],
        [
            "Python is an easy to learn powerful programming language It has efficient high-level data structures and a "
            "simple but effective approach to objectoriented programming Python elegant syntax and dynamic typing",
            "programming Python elegant syntax and dynamic typing",
            [
                "Python",
                "is",
                "an",
                "easy",
                "to",
                "learn",
                "powerful",
                "language",
                "It",
                "has",
                "efficient",
                "high-level",
                "data",
                "structures",
                "and",
                "a",
                "simple",
                "but",
                "effective",
                "approach",
                "to",
                "objectoriented",
                "programming",
            ],
        ],
    ]:
        s = data[0]
        t = data[1]
        want = data[2]
        result = missingWords(s, t)

        assert want == result, f"\ns={s}\nt={t}\nwant={want}\ngot ={result}"

    # fptr.write('\n'.join(result))
    # fptr.write('\n')
    # fptr.close()
