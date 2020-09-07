def check_possibility(a, b):
    f = (2 * b - a) / 3
    s = (2 * a - b) / 3
    if f >= 0 and s >= 0 and f.is_integer() and s.is_integer():
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    tDict = dict()
    t = int(input())  # Number of tests
    for i in range(t):  # Get all test cases
        tDict[i] = [int(x) for x in input().split()]

    for key, values in tDict.items():
        assert len(values) == 2
        check_possibility(values[0], values[1])

