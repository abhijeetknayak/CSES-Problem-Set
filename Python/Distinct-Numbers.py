n = int(input())
values = input().split(' ')

# Sets always hold unique values
out = set()

for val in values:
    out.add(val)
print(len(out))