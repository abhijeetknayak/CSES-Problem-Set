def create_permutation(n):
    if n == 1:
        print(1)
        return
    if n == 2 or n == 3:
        print("NO SOLUTION")
        return
    for i in range(2, n + 1, 2):
        print(i, end=' ')  # Print Even numbers first
    for i in range(1, n + 1, 2):
        print(i, end=' ')  # Print Odd numbers after that


if __name__ == '__main__':
    n = int(input())

    create_permutation(n)

