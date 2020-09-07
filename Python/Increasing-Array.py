def create_increasing_array(array):
    num_turns = 0
    prev_value = array[0]
    for idx in range(1, len(array)):
        if prev_value > array[idx]:  # Prev Value greater than current value
            turns = prev_value - array[idx]
            array[idx] += turns
            num_turns += turns
        prev_value = array[idx]
    print(num_turns)


if __name__ == '__main__':
    n = int(input())
    array = [int(x) for x in input().split()]

    assert len(array) == n and len(array) > 1

    create_increasing_array(array)