# if __name__ == '__main__':
#     n = int(input())
#     s = n * (n + 1) // 2
#     if s % 2 != 0:
#         print("NO")
#     elif n == 1 or n == 2:
#         print("NO")
#     else:
#         values = dict()
#         for i in range(1, n+1):
#             values[i] = [i]
#
#         exit = False
#         for i in range(1, n + 1):
#             v = values.copy()
#             for key in v:
#                 if i in v[key]:
#                     continue
#                 new_val = key + i
#                 new = v[key] + [i]
#                 values[new_val] = new
#                 if new_val == s // 2:
#                     print("YES")
#                     exit = True
#                     break
#             if exit:
#                 break
#         if not exit:
#             print("NO")
#         else:
#             l = len(values[s // 2])
#             print(l)
#             for val in values[s // 2]:
#                 print(val, end=' ')
#             print()
#             print(n - l)
#             for i in range(1, n + 1):
#                 if i not in values[s // 2]:
#                     print(i, end=' ')

def get_two_sets(n):
    s = n * (n + 1) / 2
    if s % 2 != 0:
        print("NO")
        return
    if n == 1 or n == 2:
        print("NO")
        return

    if n % 4 == 0:  # Multiple of 4
        for i in range(1, n + 1, 4):
            l1.append(i)
            l1.append(i + 3)
            l2.append(i + 2)
            l2.append(i + 1)
    else:
        for i in range(4, n + 1, 4):
            l1.append(i)
            l1.append(i + 3)
            l2.append(i + 2)
            l2.append(i + 1)
        l1.append(1)
        l1.append(2)
        l2.append(3)
    print("YES")
    print(len(l1))
    for val in l1:
        print(val, end=' ')
    print()
    print(len(l2))
    for val in l2:
        print(val, end=' ')

if __name__ == '__main__':
    l1 = []
    l2 = []

    n = int(input())

    get_two_sets(n)

