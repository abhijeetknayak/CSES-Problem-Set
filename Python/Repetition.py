import time

def process_input(sequence):
    assert len(sequence) > 0
    prev_char = sequence[0]
    max_len = 0
    cur_len = 0

    for char in sequence:
        if char is prev_char:
            cur_len += 1
            max_len = max(cur_len, max_len)
        else:
            cur_len = 1
            prev_char = char

    print(max_len)

if __name__ == '__main__':
    sequence = input()

    # start_time = time.process_time()
    process_input(sequence)
    # print("Took {}s".format(time.process_time() - start_time))


