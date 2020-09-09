n = int(input())
values = [int(x) for x in input().split()]

first_sum = 0
max_sum = None
for idx in range(len(values)):
    first_sum += values[idx]
    if max_sum is None:
        max_sum = first_sum
    elif first_sum > max_sum:
        max_sum = first_sum

    if first_sum < 0:
        first_sum = 0
print(max_sum)
