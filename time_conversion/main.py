#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#


def timeConversion(s):
    if not s or len(s) != 10:
        return None

    split = s.split(":")
    hour = int(split[0])
    minute = split[1]
    is_am = "A" in split[2]
    seconds = split[2].rstrip("AM" if is_am else "PM")

    if is_am:
        hour = 0 if hour == 12 else hour
    else:
        hour = 12 + (0 if hour == 12 else hour)

    return f"{hour:02d}:{minute}:{seconds}"


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # s = input()

    for s in [
        "12:01:00PM",
        "12:01:00AM",
        "07:05:45PM",
        "08:10:11AM",
        "11:11:11PM"
    ]:
        result = timeConversion(s)
        print(s, " -> ", result)

    # fptr.write(result + '\n')

    # fptr.close()
