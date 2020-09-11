from itertools import permutations

def create_string(seq):
    n = len(seq)
    p = set(map("".join, permutations(seq, n)))  # Length of string will be used

    print(len(p))
    for strings in sorted(p):
        print(strings)


if __name__ == '__main__':
    sequence = input()

    create_string(sequence)