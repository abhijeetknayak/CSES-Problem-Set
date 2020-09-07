def get_value(X, Y):
    m = max(X, Y)
    diag = 1
    # Now find diagonal element for (m, m). This will be the reference
    # diag(0, 0) = 1
    # diag(1, 1) = 1 + 2 (i = 0)
    # diag(2, 2) = 3 + 2 * 2 (i = 1)
    diag = m * (m - 1) + 1
    if Y == m:  # The row value is the max value. Increment diagonal value with the difference (m - Y)
        print(diag + (m - X))
    else:  # The col value is the max value. Decrease difference (m - X) from the diagonal value
        print(diag - (m - Y))



if __name__ == '__main__':
    t = int(input())  # Number of tests
    tDict = dict()
    for i in range(t):
        tDict[i] = [int(x) for x in input().split()]

    #  Stored all test cases : X and Y values
    for key, value in tDict.items():
        assert len(value) == 2
        get_value(value[0], value[1])