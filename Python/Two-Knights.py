def get_ways_knights(n):
    ways = 0
    print(ways)  # For n = 1
    for i in range(2, n + 1):
        ways = i**2 * (i**2 - 1) // 2
        if i > 2:
            ways -= 2 * 2 * (i - 1) * (i - 2)
        print(ways)

def get_ways_pawn(n):
    ways = 0
    print(ways)  # For n = 1
    for i in range(2, n + 1):
        ways = i**2 * (i**2 - 1) // 2
        ways -= 2 * 2 * (i - 1) * (i - 1)
        print(ways)


if __name__ == '__main__':
    n = int(input())

    get_ways_knights(n)

    # get_ways_pawn(n)