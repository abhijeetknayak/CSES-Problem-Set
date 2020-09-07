def find_trailing_zeros(number):
    count = 0
    while number % 5 == 0:  # Divisible by 5
        count += number // 5
        number = number // 5
    print(count)

if __name__ == '__main__':
    n = int(input())

    find_trailing_zeros(n)