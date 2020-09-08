import time

def process_input(val):
    print(val, end=' ')
    while val != 1:
        if val % 2 == 0:
            val = val // 2
            print(val, end=' ')
        else:
            val = val * 3 + 1
            print(val, end=' ')

if __name__ == '__main__':
    n = int(input())

    # Check time taken
    # start_time = time.process_time()
    process_input(n)
    # t = time.process_time() - start_time
    # print()
    # print("Took {}s".format(t))
