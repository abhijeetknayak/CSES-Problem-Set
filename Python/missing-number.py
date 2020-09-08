import time

def process_input(numbers, n):
    s = 0
    for i in range(len(numbers)):
        s += numbers[i]
    print(n * (n + 1) // 2 - s)

if __name__ == '__main__':
    n = int(input())
    num = [int(x) for x in input().split()]

    assert len(num) == n - 1

    process_input(num, n)

    # start_time = time.process_time()
    ''' for val in range(1, n + 1):
        try:
            num.remove(val)
        except:
            print(val)
            break '''
    # print("Took {}s".format(time.process_time() - start_time))


