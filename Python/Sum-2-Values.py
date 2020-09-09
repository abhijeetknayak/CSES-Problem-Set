n_s = [int(x) for x in input().split(' ')]
n = n_s[0]
s = n_s[1]

values = [int(x) for x in input().split(' ')]

printVal = False
idx, idx1 = 0, 0
results = dict()
for idx, value in enumerate(values):
    if s - values[idx] in results:
        print(results[s - values[idx]] + 1, idx + 1)
        printVal = True
    else:
        results[values[idx]] = idx
if not printVal:
    print("IMPOSSIBLE")