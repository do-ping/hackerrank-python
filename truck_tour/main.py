#!/bin/python3


#
# Complete the 'truckTour' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY petrolpumps as parameter.
#


def truckTour(petrolpumps):
    start_pump_i = 0
    current_pump_i = 0
    truck_capacity = 0

    while start_pump_i < len(petrolpumps):
        truck_capacity += petrolpumps[current_pump_i][0]
        truck_capacity -= petrolpumps[current_pump_i][1]
        if truck_capacity < 0:
            start_pump_i = current_pump_i + 1
            current_pump_i = start_pump_i
            truck_capacity = 0
            continue

        current_pump_i = (current_pump_i + 1) % len(petrolpumps)
        if current_pump_i == start_pump_i:
            return start_pump_i

    return None


if __name__ == "__main__":
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    # n = int(input().strip())
    # petrolpumps = []
    # for _ in range(n):
    #     petrolpumps.append(list(map(int, input().rstrip().split())))

    for input_ in [([[1, 5], [10, 3], [3, 4]], 1)]:
        petrolpumps = input_[0]
        expected = input_[1]
        result = truckTour(petrolpumps)
        print(petrolpumps, expected, result)
        assert expected == result

    # fptr.write(str(result) + '\n')
    # fptr.close()
