n = int(input())
sorted_list = []
for i in range(n):
    v = [int(x) for x in input().split()]
    if not sorted_list:
        sorted_list.append(v)
    else:
        for idx in range(len(sorted_list)):
            if sorted_list[idx][1] > v[1]:
                sorted_list.insert(idx, v)
                break
            else:
                if idx == len(sorted_list) - 1:
                    sorted_list.insert(idx + 1, v)
                    break
                else:
                    continue
cur_time = 0
count = 0

for val in sorted_list:
    if val[0] >= cur_time:
        cur_time = val[1]
        count += 1
print(count)