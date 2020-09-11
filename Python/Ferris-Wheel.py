n_x = [int(x) for x in input().split()]
n = n_x[0]
x = n_x[1]

weights = [int(x) for x in input().split()]
weights.sort()
count = 0
first, last = 0, len(weights) - 1
while first <= last:
    if first == last:
        count += 1
        first += 1
        last -= 1
    elif weights[first] + weights[last] > x:
        count += 1
        last -= 1
    else:
        count += 1
        first += 1
        last -= 1
print(count)

