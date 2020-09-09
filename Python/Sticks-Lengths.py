n = int(input())
stick_len = [int(x) for x in input().split()]

stick_len.sort()
if n % 2 != 0:  # Odd number of sticks
    median = stick_len[n // 2]
else:  # Even number of sticks
    median = (stick_len[n // 2] + stick_len[n // 2 - 1]) // 2
cost = 0
for l in stick_len:
    cost += abs(l - median)
print(cost)