def reorder(sequence):
    alpha = dict()
    odd_count = 0
    for char in sequence:
        if char in alpha:
            alpha[char] += 1
        else:
            alpha[char] = 1
    for key, values in alpha.items():
        if values % 2 != 0:  # Odd number of characters
            odd_count += 1
    if odd_count > 1:
        print("NO SOLUTION")
        return
    output = None
    for key, values in alpha.items():
        if values % 2 == 0:  # Even count
            for i in range(values // 2):
                if output is None:
                    output = key
                else:
                    output += key
    if output is not None:
        print(output, end='')
    for key, values in alpha.items():
        if values % 2 != 0:
            for i in range(values):
                print(key, end='')
    # Reverse Output
    if output is not None:
        print(output[::-1])

if __name__ == '__main__':
    sequence = input()

    reorder(sequence)

